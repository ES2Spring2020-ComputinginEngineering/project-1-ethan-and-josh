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

"""
Created on Wed Mar  4 20:31:21 2020

import os
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.signal as sig

path = "/Users/Joshuabalbi/Documents/"
os.chdir(path)



array1= np.loadtxt('18inch.txt',delimiter=',')
time=array1[:,3]
x=array1[:,0]
y=array1[:,1]
z=array1[:,2]
x_y= array1[:,0:2]
plt.plot(time,x_y/1000)
plt.xlabel('time')
plt.ylabel('acceleration x and y')
plt.title('13.5inch', fontdict=None, loc='center')

def find_theta(x,y):
    A1= np.sqrt((x/1000)**2+(y/1000)**2)
    Ag=9.81
    theta = math.asin(A1/Ag)
    return theta


def newlist(x):
    list_theta=[]
    for i in range(0,x):
        theta = find_theta(array1[i,0],array1[i,1]) 
        list_theta.append(theta)
    return list_theta 
#   
#plt.plot(time,newlist(264))
#plt.xlabel('time')
#plt.ylabel('theta')
#plt.title('18inch', fontdict=None, loc='center')

list_theta_filt = sig.medfilt(newlist(264))
list_theta_pks, _ = sig.find_peaks(list_theta_filt)

#print(list_theta_pks)
#print(time)

list_theta_pks= list(list_theta_pks)

def time_peaks():
    t=[]
    for i in list_theta_pks:
            l=array1[i,3]
            t.append(l)
    return t            

def period():
    av=[]
    for i in range(2,11):
        j=time_peaks()[i]-time_peaks()[i-2]
        av.append(j)
    return av

def added_period():
    i=0
    total=0
    while(i < len(period())): 
        total = total + period()[i] 
        i += 1
    return total
        
print(added_period()/len(period()))


    
plt.plot([0.305,0.3429,0.381,0.4191,0.4572],[1.1674000000000002,1.2336000000000003,1.2861999999999998,1.3404,1.385888888888889])
plt.axis([.25,.55,1,1.5])
plt.xlabel('lenght')
plt.ylabel('period')
plt.title('Length vs. Period experimental', fontdict=None, loc='center')
