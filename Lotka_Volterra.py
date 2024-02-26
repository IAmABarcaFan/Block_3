import sys
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

# Please note that any whitespace in the filepath/argument will bug out sys.argv, as it treats them as different arguments.
list_of_arguments = sys.argv

# Using a sample of 1000 prey (x) and predator (y) each.
x = 1000
y = 1000
# Preset values for model parameters here.
alpha_set = 0.15
beta_set = 0.4
delta_set = 0.35
gamma_set = 0.2
# Let's solve for 100 time steps
t_max = 100
# Create a tuple to represent the initial conditions
init_cond = [x, y]

def arg_cleanup():
    '''
    Terminal input cleanup. It seperates the terminal inputs into sorted nested lists.
    Output:
        list_flags: List of flag inputs in terminal (List)
        nested_arguments: Nested list of flags and their values input in terminal (Nested List)
    '''
    list_of_arguments.pop(0)  # Gets rid of the name of file
    list_flags = [x for x in list_of_arguments if x.startswith("--", 0, 3)]

    nested_arguments = []
    current_sublist = []
    for arg in list_of_arguments:  # need to fix
        if arg.startswith("--"):
            if current_sublist:
                nested_arguments.append(current_sublist)
            current_sublist = [arg]
        else:
            current_sublist.append(arg)

    if current_sublist:
        nested_arguments.append(current_sublist)

    return list_flags, nested_arguments

def diff_eq(init, t, alpha, beta, delta, gamma):
    '''
    Calculates the gradient for the Lotka-Volterra model
    Inputs:
        init: state of the system, with init[0] = number of prey
                                        init[1] = number of predator
        t: current time- not used here, but odeint expects to pass this argument so we must include it
        alpha: the rate of growth of prey
        beta: the rate of death of prey
        delta: the rate of growth of predator
        gamma: the rate of death of predator
    Outputs:
        the gradient of the Lotka-Volterra model
    '''
    print(init[0], init[1], alpha, beta, delta, gamma)  # testing, TypeError: can't multiply sequence by non-int of type 'numpy.float64'
    dxdt = alpha * init[0] - beta * init[0] * init[1]
    dydt = delta * init[0] * init[1] - gamma * init[1]
    grad = [dxdt, dydt]
    return grad

def solve_diff_eq(init, t_max, alpha, beta, delta, gamma):
    '''
    Solves the Lotka-Volterra model using odeint.
    '''
    t = np.linspace(0, t_max)
    xy_list = odeint(diff_eq, init, t, (alpha, beta, delta, gamma))
    return xy_list, t  # sir is a nested list of both values at different points in time.

def plot_diff_eq(t, data, fig, num):
    ax = fig.add_subplot(1, len(alpha_set), num)
    ax.plot(t, data[0], label='x')  # Plots x
    ax.plot(t, data[1], label='y')  # Plots y
    ax.set_title('Lotka-Volterra Model When Alpha = '+str(alpha_set[num]))
    ax.set_xlabel('Time')
    ax.set_ylabel('Number of Animal Present')
    ax.legend()

def main():
    global x, y, alpha_set, beta_set, delta_set, gamma_set, init_cond
    list_flag, nested_arguments = arg_cleanup()

    for index, flag in enumerate(list_flag): 
        if flag=="--initial":
            # Allow user to set initial populations for both species.
            x = int(nested_arguments[index][1])
            y = int(nested_arguments[index][2])
            init_cond = [x, y]

        elif flag=="--alpha":
            # Allow user to set value(s) for alpha. (List of values)
            alpha_set = nested_arguments[index] 
            alpha_set.pop(0)

        elif flag=='--beta':
            # Allow user to set value for beta.
            beta_set = nested_arguments[index][1]

        elif flag=='--delta':
            # Allow user to set value for delta.
            delta_set = nested_arguments[index][1]

        elif flag=='--gamma':
            # Allow user to set value for gamma.
            gamma_set = nested_arguments[index][1]
    
    list_flag_copy = [flag for flag in list_flag if flag=='--save_plot']

    # Calculation and plotting happens here.  Multiple subplots if more than one alpha.      
    if bool(list_flag_copy)==True and list_flag_copy[-1]=='--save_plot':
        # Saves the plot with the provided filename.
        fig = plt.figure()
        for num in range(len(alpha_set)):
            xy_list, t = solve_diff_eq(init_cond, t_max, alpha_set[num], beta_set, delta_set, gamma_set)
            plot_diff_eq(t, xy_list, fig, num)
        plt.savefig(str(nested_arguments[-1][1]))

    elif bool(list_flag_copy)==False:
        # Show the plot.
        fig = plt.figure()
        for num in range(len(alpha_set)):
            xy_list, t = solve_diff_eq(init_cond, t_max, alpha_set[num], beta_set, delta_set, gamma_set)
            plot_diff_eq(t, xy_list, fig, num)
        plt.show()
        

if __name__ == "__main__":
    main()