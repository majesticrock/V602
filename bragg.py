import numpy as np 
import math
import pandas as pd
from uncertainties import ufloat
from uncertainties import unumpy as unp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
h = 4.136e-15
c = 299792458
d = 2.014e-10
theta = ufloat(10.8, 0.35) *np.pi/180 
#theta = 22.5 *np.pi/180
#theta = 20.29 *np.pi/180
thetab = ufloat(20.00, 0,35) *np.pi/180
thetaa = ufloat(22.21, 0.35) *np.pi/180
K = 8979
R = 13.8


E = h * c / (2 * d * unp.sin(theta))
Ea = h * c / (2 * d * unp.sin(thetaa))
Eb = h * c / (2 * d * unp.sin(thetab))
print(E)
sig1 = 40 - unp.sqrt(E/R)
print("sig11", sig1)
#Wellenlänge
l = h *c / E
print(l)
#Abschirmkonstante Kupfer
sig1 = 29 - unp.sqrt(K/R)
print("sig1", sig1)

#sig2 = 29 - 2 * unp.sqrt((R* (29-sig1)**2 - Ea)/R)
#print("sig2", sig2)
#sig3 =  29 - 2 * unp.sqrt((R* (29-sig2)**2 - E)/R)

delE = np.cos(4.7 * np.pi/180) / (np.sin(4.7 * np.pi/180))**2 * h * c / (2 * d) * (0.35 * np.pi/180)
print(delE)
dell = h * c / 3.76**2 * delE
print(dell)
a = ufloat(22.06, 0.35)
b = ufloat(22.64, 0.35)
print(b-a)

t1 = ufloat(20.00, 0.35)
t2 = ufloat(20.44, 0.35)
print(t1 - t2)