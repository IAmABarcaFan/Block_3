import argparse
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
# '''
# ==============================================================================================================
# This section contains code for the Ising Model - task 1 in the assignment
# ==============================================================================================================
# '''

parser = argparse.ArgumentParser(description='The Ising Model')
parser.add_argument('-ising_model', action='store_true')
parser.add_argument('-external', nargs=1)
parser.add_argument('-alpha', nargs=1)
parser.add_argument('-test_ising', action='store_true')
args = parser.parse_args()

def argument_cleanup():
    '''
    Cleans up the 'external' and 'alpha' command line inputs for further use.
    Returns floats/integers.
    '''
    if not (args.external or args.alpha):  # Not alpha, not external
        alpha = 1
        external = 0
    elif args.external and not args.alpha:  # Only external
        alpha = 1
        external = float(args.external[0])
    elif args.alpha and not args.external:  # Only alpha
        alpha = float(args.alpha[0])
        external = 0
    else:  # Alpha and external
        alpha = float(args.alpha[0])
        external = float(args.external[0])
    
    return alpha, external

def array_maker(size=50):
    '''
    The function creates and returns a square, random array of specified size. Input should be an integer only.
    '''
    array = np.random.choice([-1, 1], size=(size, size))  # Generate a random array of size 50x50 with values between 0 and 1

    return array    

def get_neighbours(arr, row, col):
    '''
    Returns a list of the top, bottom, left, right neighbours.
    '''
    neighbours = []

    # Determine array dimensions
    num_rows, num_cols = arr.shape

    if row > 0:  # Top neighbour
        neighbours.append(arr[row - 1, col])

    if row < num_rows - 1:  # Bottom neighbour
        neighbours.append(arr[row + 1, col])

    if col > 0:  # Left neighbour
        neighbours.append(arr[row, col - 1])

    if col < num_cols - 1:  # Right neighbour
        neighbours.append(arr[row, col + 1])

    return neighbours


def calculate_agreement(population, row, col, external=0.0):
    '''
    This function should return the *change* in agreement that would result if the cell at (row, col) was to flip it's value
    Inputs: population (numpy array)
            row (int)
            col (int)
            external (float) -> H in the document
            alpha (float/int)
    Returns:
            change_in_agreement (float)
    '''
    #Your code for task 1 goes here - take array and get neighbour, calculation
    list_neighbours = get_neighbours(population, row, col)
    D_i = 0

    for neighbour in list_neighbours:  # D_i calculation
        D_i += population[row, col]*neighbour
    D_i += external*population[row, col]

    return D_i  # The flipping mechanism is unclear?

def ising_step(population, external=0.0, alpha=1):
    '''
    This function will perform a single update of the Ising model
    Inputs: population (numpy array)
            external (float) - optional - the magnitude of any external "pull" on opinion
            alpha (float/int)
    '''	
    n_rows, n_cols = population.shape  # Dimensions of the numpy array.
    row = np.random.randint(0, n_rows)  # Picks a random point in the numpy array
    col  = np.random.randint(0, n_cols)

    agreement = calculate_agreement(population, row, col, external)
    probability = math.exp(agreement / alpha)  # Probability calculation

    if agreement < probability:
        population[row, col] *= -1  # Flips the point in the array if surrounding disagree. Need to check if correct?
            
    #Your code for task 1 goes here
    return population
            

def plot_ising(im, population):  # Why is this not implemented in the main function?
    '''
    This function will display a plot of the Ising model
    '''
    new_im = np.array([[255 if val == -1 else 1 for val in rows] for rows in population]).astype(np.int8)
    im.set_data(new_im)
    plt.pause(0.01)  # The original time is 0.1


def test_ising():
    '''
    This function will test the calculate_agreement function in the Ising model
    '''
    print("Testing ising model calculations")
    population = -np.ones((3, 3))  # Gives a 3x3 array of -1
    assert(calculate_agreement(population,1,1)==4), "Test 1"

    population[1, 1] = 1.
    assert(calculate_agreement(population,1,1)==-4), "Test 2"

    population[0, 1] = 1.
    assert(calculate_agreement(population,1,1)==-2), "Test 3"

    population[1, 0] = 1.
    assert(calculate_agreement(population,1,1)==0), "Test 4"

    population[2, 1] = 1.
    assert(calculate_agreement(population,1,1)==2), "Test 5"

    population[1, 2] = 1.
    assert(calculate_agreement(population,1,1)==4), "Test 6"

    "Testing external pull"
    population = -np.ones((3, 3))
    assert(calculate_agreement(population,1,1,1)==3), "Test 7" 
    assert(calculate_agreement(population,1,1,-1)==5), "Test 8"
    assert(calculate_agreement(population,1,1,-10)==14), "Test 9"  # The values provided for test 9 and 10 in the original code, was reversed.
    assert(calculate_agreement(population,1,1,10)==-6), "Test 10"

    print("Tests passed")


def ising_main(population, alpha=None, external=0.0):    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_axis_off()
    im = ax.imshow(population, interpolation='none', cmap='RdPu_r') 


    # Iterating an update 100 times
    for frame in range(100):
        # Iterating single steps 1000 times to form an update
        for step in range(1000):
            ising_step(population, external, alpha)
        print('Step:', frame, end='\r')
        plot_ising(im, population)
        # im.set_array(population)  # Update the displayed image
        # plt.pause(0.01)  # Pause to allow the plot to update

    plt.show()  # Show the plot after all update

# Testing
if __name__ == '__main__':
    if args.ising_model:
        alpha, external = argument_cleanup()  # Gets the variables used below
        ising_main(array_maker(50), alpha, external)  # Runs the main function. Change the number for diff size arrays.
    
    if args.test_ising:
        test_ising()
