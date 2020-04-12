# Project 1 --- ES2
# Part 5

# FILL THESE COMMENTS IN
#*****************************************
# YOUR NAME: Ethan Donnelly/Joshua Balbi
# NUMBER OF HOURS TO COMPLETE: 5
# YOUR COLLABORATION STATEMENT(s): Ethan Donnelly and Joshua Balbi.
#
#
#*****************************************


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

#The function change_graph has parameters x,v,a,t,L.
#Gets the next acceleration with a time step of .05 seconds.
#The return values are each of the new varables being calculated at the new time.

    A1 = -(g / L) * math.sin(x)
    V1 = v + (A1 * dt)
    X1 = x + (V1 * dt)
    T1 = t + dt
    return X1, V1, A1, T1

def Convert(n):

#The function Convert has the parameter n.
#This function makes more time steps. i is a time step and it is being calculayed over 10 seconds.
#The return value is a list of the new values for each time step. 

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

#These lists assign each of the values in the list to their respective variable at each time step.
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

#The function time_peaks has the parameter n.
#This functions finds all the values of t when theta hits a maximum.
#It returns a list of times when theta is a maximum. 

    t=[]
    for i in list_theta_pks:
        list_t=(Convert(n)[3::4])
        l=list_t[i]
        t.append(l)
    return t            



def period(n):

#This function period has the parameter n.
#It finds the times when theta is a max and subtracts them from each other to find the period of each.
#The return value is a list of all the periods within the simulation.

    av=[]
    for i in range(2,6):
        j=time_peaks(n)[i]-time_peaks(n)[i-1]
        av.append(j)
    return av

def added_period(n):

#This function added_period has the parameter n. 
#It adds up all the periods of the function.
#The return value is the total of all the periods added up.

    i=0
    total=0
    while(i < len(period(n))): 
        total = total + period(n)[i] 
        i += 1
    return total

P=[]
#this for loop finds the average length of the simulated periods in the function. 
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
