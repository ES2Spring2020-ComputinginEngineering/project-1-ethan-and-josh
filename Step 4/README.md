import os
import matplotlib.pyplot as plot
import math
import numpy as np

path = ("C:\\Users\\ethan\\Desktop\\project-1-ethan-and-josh\\Step 4\\Data\\data_capture")
os.chdir(path)

fin1 = open("12inch.csv" , "r")
fin2 = open("13.5inch.csv" , "r")
fin3 = open("15inch.csv" , "r")
fin4 = open("16.5inch.csv" , "r")
fin5 = open("18inch.csv" , "r")

data_file = nploadtext(datafile.txt,delimiter=',')
time=datatfile[:,3]
x=datatfile[:,0]
y=datatfile[:,1]
z=datatfile[:,2]
x_y= datatfile[:,0:2]
plt.plot(x_y,time)
plt.xlabel('acceleration x and y')
plt.ylabel('time')
                         



