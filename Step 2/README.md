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

def theory(l):

#def_theory is a function that has the parameter 1.
#It uses an equation to find a value.
#The return value is the result of .4572 plugged into the equation.

    return((2*np.pi)*np.sqrt(l/9.81))
    
print(theory(0.4572))


plt.plot([0.305,0.3429,0.381,0.4191,0.4572],[theory(0.305),theory(0.3429),theory(0.381),theory(0.4191),theory(0.4572)])
plt.axis([.25,.55,1,1.5])


0.305
0.3429
0.381
0.4191
0.4572
