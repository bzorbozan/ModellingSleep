# MAT 231 PROJECT 2
# goal is to get a solution for H.

import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# define global variables
T = 24/24      # hrs ( 1 day period )
t_wakeup = 8.75/ 24      
t = t_wakeup         # time. 
alpha = t_wakeup 

Xw = 59.55/24      # convert from hrs to days
Xs = 4.2/ 24       # convert from hrs to days

h0_plus = 0.3        #0.6
h0_minus = 0.05
a = 0.02

ss = 0.001    # step size for euler's method.

max_no_of_days = 3

t_array = []
H_array = []

draw_bounds = True      #bools are capitalized in python!!

# define functions

def deriv_while_awake (H):
    return (1-H)/Xw

    
def deriv_while_asleep (H):
    return (-H/Xs)

def euler_H (x, H, deriv):
    
    # iterate y value (H)
    H_new = H + deriv * ss
    
    # iterate x value 
    x += ss
    
    #print(str(t) + "," + str(H))
    
    return (x, H_new)     # returns tuple

def Ct (x):
    return math.sin( ( 2 * math.pi / T ) * (x - alpha) )

def H_plus(x):
    return h0_plus + a * Ct(x)
  
def H_minus(x):
    return h0_minus + a * Ct(x)

H = H_minus(t)   # STARTING Y VALUE (H) GETS INITIALIZED HERE. We assume that it starts awake.
phase = 0

while (phase < max_no_of_days):
    while (H_plus(t) > H):     # 0.05 is some tolerance
        # update vals of t and H by tuple unpacking
        (t, H) = euler_H(t, H, deriv_while_awake(H))
        t_array.append(t)
        H_array.append(H)
        print(str(t) + "," + str(H))
        
    print("FALLING ASLEEP")
    
    while (H_minus(t) < H):     # 0.05 is some tolerance
        # update vals of t and H by tuple unpacking
        (t, H) = euler_H(t, H, deriv_while_asleep(H))
        t_array.append(t)
        H_array.append(H)        
        print(str(t) + "," + str(H))
        
    print("WAKING UP")
    phase += 1
    


# GRAPHING THE BOUNDS

# H minus

# we want to use range() func for floats so we convert days --> hrs --> frac of days 
Hmin_tlist = list(range(0, max_no_of_days * 24))
Hmin_list =[]
i= 0
for ele in Hmin_tlist:
    Hmin_tlist[i] = ele/24 + t_wakeup 
    i += 1
for ele in Hmin_tlist:
    Hmin_list.append(H_minus(ele))
    

# now do the same for H plus
Hpls_tlist = list(range(0, max_no_of_days * 24))
Hpls_list =[]
i= 0
for ele in Hpls_tlist:
    Hpls_tlist[i] = ele/24 + t_wakeup 
    i += 1
for ele in Hpls_tlist:
    Hpls_list.append(H_plus(ele))


# GRAPH COMMANDS

plt.plot(t_array, H_array)

if draw_bounds:
    plt.plot(Hmin_tlist, Hmin_list)
    plt.plot(Hpls_tlist, Hpls_list)

#plt.xticks(list(range(0, max_no_of_days * 24))
#plt.xlim(0,72)
plt.title("Modelling College Students' Sleep\nSleepiness vs Time (days)")
plt.xlabel("time (days)")
plt.ylabel("H (sleepines)")
#plt.xticks(t)
#plt.yticks(H)


plt.show()