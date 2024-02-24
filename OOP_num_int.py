import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#This function defines the right hand side of the equation we want to integrate
def gradient(N, t, alpha, beta):
    return -alpha*N + beta*N
#Lets start with an initial population of 100 people
N0 = 100
#We also need some values for our parameters
alpha = [0.1, 0.05, 0.075]
beta = [0.05, 0.1, 0.075]
#We need to tell scipy which timesteps to use for the integration- linspace will give us evenly spaced points
t = np.linspace(0, 100)
fig = plt.figure()
for num_1 in range(len(alpha)):
    for num_2 in range(len(beta)):
        N = odeint(gradient, N0, t, (alpha[num_1], beta[num_2]))
        ax = fig.add_subplot(len(alpha), len(beta), num_1*3+num_2+1, title=str(alpha[num_1])+' '+str(beta[num_2]))
        ax.plot(t, N)
        ax.set_ylabel("Population size (N people)")
        ax.set_xlabel("Time (months)")
plt.show()