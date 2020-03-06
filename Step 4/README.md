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

def create_array(name):
    
    fin = open(name, "r")
    outname = "new" + name
    fout = open(outname, "w")
#    for line in fin:
 #       line = line.replace(",", "")
  #      fout.write(line)
    fin.close()
    fout.close()
    
    array = np.loadtxt(outname, dtype = int)
    print(array)
    new_array = array[0,0]
    print(new_array)
                         
create_array("12inch.csv")

#plt.plot (Links to an external site.)([listx,listy], [time], 'ro')
#plt.axis (Links to an external site.)([0, 6, 0, 20])
#plt.show (Links to an external site.)()
