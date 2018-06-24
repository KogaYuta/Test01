# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 14:47:19 2017

@author: yuta
"""

from qutip import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution

def ackley(x):
     arg1 = -0.2 * np.sqrt(0.5 * (x[0] ** 2 + x[1] ** 2))
     arg2 = 0.5 * (np.cos(2. * np.pi * x[0]) + np.cos(2. * np.pi * x[1]))
     return -20. * np.exp(arg1) - np.exp(arg2) + 20. + np.e
bounds = [(-5, 5), (-5, 5)]
result = differential_evolution(ackley, bounds)
result.x, result.fun

b = [(-np.pi-0.1,np.pi+0.1)]
a = differential_evolution(np.cos,b)

#electron spin/nitrogen spin/carbon spin
ppu=tensor(plus1,plus1,up)
ppd=tensor(plus1,plus1,dw)
p0u=tensor(plus1,zero,up)
p0d=tensor(plus1,zero,dw)
pmu=tensor(plus1,minus1,up)
pmd=tensor(plus1,minus1,dw)
mpu=tensor(minus1,plus1,up)
mpd=tensor(minus1,plus1,dw)
m0u=tensor(minus1,zero,up)
m0d=tensor(minus1,zero,dw)
mmu=tensor(minus1,minus1,up)
mmd=tensor(minus1,minus1,dw)





