import sys
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

# Please note that any whitespace in the filepath/argument will bug out sys.argv, as it treats them as different arguments.
# Terminal input cleanup
list_of_arguments = sys.argv

# Using a sample of 1000 prey (x) and predator (y) each.
x = 1000
y = 1000
# Set values for model parameters here.
alpha_set = 0.15
beta_set = 0.4
delta_set = 0.35
gamma_set = 0.2
# Let's solve for 100 time steps
t_max = 100
#Create a tuple to represent the initial conditions
init_cond = (x, y)

def arg_cleanup():
    list_of_arguments.pop(0)  # Gets rid of the name of file
    list_flags = [x for x in list_of_arguments if x.startswith("--", 0, 3)]

    nested_arguments = []
    for arg in list_of_arguments:
        if arg.startswith("--", 0, 3):
            argument_list = []  # Add arguments to the list until meeting another flag, then append to nested_arguments
            nested_arguments.append(argument_list)

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
    dxdt = alpha * init[0] - beta * init[0] * init[1]
    dydt = delta * init[0] * init[1] - gamma * init[1]
    grad = [dxdt, dydt]
    return grad

def solve_diff_eq(sir0, t_max, alpha, beta, delta, gamma):
    '''
    Solves the Lotka-Volterra model using odeint.
    '''
    t = np.linspace(0, t_max)
    sir = odeint(diff_eq, sir0, t, (alpha, beta, delta, gamma))
    return sir, t  # sir is a nested list of both values at different points in time.

def plot_diff_eq(t, data):
    # The figure should be created outside function and for loop.
    # The function should be called inside (enumerated) for loop.
    a = 'Placeholder'

def main():
    list_flag, nested_arguments = arg_cleanup()

    for flag in list_flag:  # Currently the flag system only works if --save_plot is the last flag given
        if flag=="--initial":
            # Allow user to set initial populations for both species.
            a = 'Placeholder'
        elif flag=="--alpha":
            # Allow user to set value(s) for alpha. Multiple subplots if more than one alpha.
            a = 'Placeholder'
        elif flag=='--beta':
            # Allow user to set value for beta.
            a = 'Placeholder'
        elif flag=='--delta':
            # Allow user to set value for delta.
            a = 'Placeholder'
        elif flag=='--gamma':
            # Allow user to set value for gamma.
            a = 'Placeholder'
        
        list_flag.remove(str(flag))
             
    if bool(list_flag)==True and list_flag[0]=='--save_plot':
        # Saves the plot with the provided filename.
        a = 'Placeholder'
    elif bool(list_flag)==False:
        # Show the plot.
        a = 'Placeholder'
        

if __name__ == "__main__":
    main()