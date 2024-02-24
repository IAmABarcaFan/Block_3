import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

#Let's use a population of 1000 people
N = 1000
#S represents the number of susceptible people; we'll start our model with one infected, with means S=N-1 S = N-1
S = N-1
#I represents the number of infected people; we'll leave start this at one.
I = 1
#R represents the number of people removed (either due to recovery or death). We start this at zero. R=0
R = 0

def diff_sir(sir, t, beta, gamma):
    '''
    Calculates the gradient for an SIR model of disease spread
    Inputs:
            sir: state of the system, with sir[0] = number susceptible
                                           sir[1] = number infected
                                           sir[2] = number recovered
            t: current time- not used here, but odeint expects to pass this argument so we must include it
            beta: the rate at which the virus spreads
            gamma: the rate at which people are removed due to the virus
    Outputs:
            the gradient of the SIR model
    '''
    dsdt = (-beta*sir[0] * sir[1])/N
    didt = (beta*sir[0]*sir[1])/N - (gamma * sir[1])
    drdt = gamma * sir[1]
    grad = [dsdt, didt, drdt]
    return grad

def diff_sis(sir, t, beta, gamma):
    dsdt = (-beta*sir[0] * sir[1])/N + gamma * sir[1]
    didt = (beta*sir[0]*sir[1])/N - (gamma * sir[1])
    drdt = 0
    grad = [dsdt, didt, drdt]
    return grad

def solve_sir(sir0, t_max, beta, gamma):
    '''
    Solves an SIR model using odeint.
    '''
    t = np.linspace(0, t_max)
    sir = odeint(diff_sir, sir0, t, (beta, gamma))
    return sir, t  # sir is a nested list of all three values at different points in time.

def solve_sis(sir0, t_max, beta, gamma):
    t = np.linspace(0, t_max)
    sis = odeint(diff_sis, sir0, t, (beta, gamma))
    return sis, t

def plot_sir_sis(t, data, data_2):
        fig = plt.figure()
        ax1 = fig.add_subplot(311)
        ax1.plot(t, data[:, 0], label='S(t) SIR Model')  # data[:, 0] is the list of first elements of elements in 'sir'
        ax1.plot(t, data_2[:, 0], label='S(t) SIS Model')
        ax1.set_title('Susceptable')
        ax1.legend()
        ax2 = fig.add_subplot(312)
        ax2.plot(t, data[:, 1], label='I(t) SIR Model')
        ax2.plot(t, data_2[:, 1], label='I(t) SIS Model')
        ax2.legend()
        ax2.set_title('Infected')
        ax3 = fig.add_subplot(313)
        ax3.plot(t, data[:, 2], label='R(t) SIR Model')
        ax3.legend()
        ax3.set_title('Recovered/Removed')
        plt.show()

def main():
    #Set values for model parameters here.
    beta = 0.4
    gamma = 0.2
    #Let's solve for 100 time steps
    t_max = 100
    #Create a tuple to represent the initial conditions
    sir0 = (S, I, R)
    #Solve the model
    sir, t = solve_sir(sir0, t_max, beta, gamma)
    sis, t_2 = solve_sis(sir0, t_max, beta, gamma)
    #Plot the results
    plot_sir_sis(t, sir, sis)
    return t_2

if __name__ == "__main__":
        main()