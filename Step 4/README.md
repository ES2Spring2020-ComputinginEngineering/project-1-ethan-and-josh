# Project 1 --- ES2
# Microbit Logger

# FILL THESE COMMENTS IN
#*****************************************
# YOUR NAME: Ethan Donnelly/Joshua Balbi
# NUMBER OF HOURS TO COMPLETE: 6
# YOUR COLLABORATION STATEMENT(s): Ethan Donnelly and Joshua Balbi.
#
#
#*****************************************

import os
import matplotlib.pyplot as plt
import numpy as np

path = "/Users/Joshuabalbi/Documents/"
os.chdir(path)



array1= np.loadtxt('12inch.txt',delimiter=',')
time=array1[:,3]
x=array1[:,0]
y=array1[:,1]
z=array1[:,2]
x_y= array1[:,0:2]
plt.plot(time,x_y)
plt.xlabel('time')
plt.ylabel('acceleration x and y')

                         



