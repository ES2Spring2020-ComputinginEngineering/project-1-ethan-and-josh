# -*- coding: utf-8 -*-

import numpy as np

import matplotlib.pyplot as plt

def theory(l):
    return((2*np.pi)*np.sqrt(l/9.81))
    
print(theory(0.4572))


plt.plot([0.305,0.3429,0.381,0.4191,0.4572],[theory(0.305),theory(0.3429),theory(0.381),theory(0.4191),theory(0.4572)])
plt.axis([.25,.55,1,1.5])


0.305
0.3429
0.381
0.4191
0.4572
