# Project1 Part 5 Goes Here
"""
Created on Tue Mar 24 13:24:34 2020

@author: Joshuabalbi
"""

# Write your code here :-)

import math
import matplotlib.pyplot as plt
import scipy.signal as sig

# initial values

T = 0
Tf = 10
g = 9.81
dt = .05
l = [0.305, 0.3429, 0.381, 0.4191, 0.4572]
m = 0.0036
a = 0
v = 0
x = 0


def change_graph(x, v, a, t, L):
    A1 = -(g / L) * math.sin(x)
    V1 = v + (A1 * dt)
    X1 = x + (V1 * dt)
    T1 = t + dt
    return X1, V1, A1, T1

def Convert(n):
    a = 0
    v = 0
    x = 1
    t = 0
    G=[]
    for i in range(0, 200):
        X1, V1, A1, T1= change_graph(x, v, a, t, l[n])
        G+=X1, V1, A1, T1
        x = X1
        v = V1
        a = A1
        t +=.05
    return G

list_x=(Convert(4)[0::4])
list_v=(Convert(4)[1::4])
list_a=(Convert(4)[2::4])
list_t=(Convert(4)[3::4])



plt.plot(list_t,list_x, label= "position")
plt.plot(list_t,list_v, label= "velocity")
plt.plot(list_t,list_a, label= "acceleration")
plt.xlabel('time')
plt.ylabel('X, V ,and A')
plt.title('time vs Motions 18 inch', fontdict=None, loc='center')
plt.legend(loc= "lower right")

list_theta_pks, _ = sig.find_peaks(list_x)


list_theta_pks= list(list_theta_pks)

def time_peaks(n):
    t=[]
    for i in list_theta_pks:
        list_t=(Convert(n)[3::4])
        l=list_t[i]
        t.append(l)
    return t            



def period(n):
    av=[]
    for i in range(2,6):
        j=time_peaks(n)[i]-time_peaks(n)[i-1]
        av.append(j)
    return av

def added_period(n):
    i=0
    total=0
    while(i < len(period(n))): 
        total = total + period(n)[i] 
        i += 1
    return total

P=[]
for i in range(0,5):
    list_x=(Convert(i)[0::4])
    list_theta_pks, _ = sig.find_peaks(list_x)
    list_theta_pks= list(list_theta_pks)
    P.append(added_period(i)/len(period(i)))

plt.plot(l,P)
plt.xlabel('length')
plt.ylabel('period')
plt.title('length vs period simulation', fontdict=None, loc='center')
plt.ylim(1,1.5)
plt.xlim(.25,.55)
