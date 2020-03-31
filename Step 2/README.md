# Project 1 --- ES2
# Part 2

# FILL THESE COMMENTS IN
#*****************************************
# YOUR NAME: Ethan Donnelly/Joshua Balbi
# NUMBER OF HOURS TO COMPLETE: 6
# YOUR COLLABORATION STATEMENT(s): Ethan Donnelly and Joshua Balbi.
#
#
#*****************************************

import numpy as np

import matplotlib.pyplot as plt
g=9.81
length=[0.305,0.3429,0.381,0.4191,0.4572]

def theory():

#theory is a function with no parameters.
#It solves for a list of the periods at each time step.
#The return value is a list of periods at their given times.

    n=[]
    for i in range(0,5):
        a=((2*np.pi)*np.sqrt(l[i]/g))
        n.append(a)
    return n


print(theory())
plt.plot([0.305,0.3429,0.381,0.4191,0.4572],theory())
plt.axis([.25,.55,1,1.5])
plt.xlabel('lenght')
plt.ylabel('period')
plt.title('Length vs. Period theoretical', fontdict=None, loc='center')

