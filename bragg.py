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
theta = ufloat(4.7, 0.35) *np.pi/180 
#theta = 22.5 *np.pi/180
#theta = 20.29 *np.pi/180
#thetab = 20.00 *np.pi/180
#thetaa = 22.21 *np.pi/180
R = 13.8
E = h * c / (2 * d * unp.sin(theta))
#Ea = h * c / (2 * d * np.sin(thetaa))
#Eb = h * c / (2 * d * np.sin(thetab))
print(E)
#Wellenlänge
l = h *c / E
print(l)
#Abschirmkonstante Kupfer
#sig1 = 29 - np.sqrt(Eb/R)
#print("sig1", sig1)

#sig2 = 29 - 2 * np.sqrt((R* (29-sig1)**2 - Ea)/R)
#print("sig2", sig2)
delE = np.cos(4.7 * np.pi/180) / (np.sin(4.7 * np.pi/180))**2 * h * c / (2 * d) * (0.35 * np.pi/180)
print(delE)
dell = h * c / 3.76**2 * delE
print(dell)
a = ufloat(22.06, 0.35)
b = ufloat(22.64, 0.35)
print(b-a)