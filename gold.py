import numpy as np 
import math
import pandas as pd
from uncertainties import ufloat
from uncertainties import unumpy as unp

R = 13.6
alpha = 7.297e-3
z = 79
c=3*10**8
h=4.135*10**(-15)
d=201.4*10**(-12)

theta3 = ufloat(15.2, 0.35)
theta2 = ufloat(13, 0.35)
lam3 = 2 * d * unp.sin(theta3*(np.pi/180))
lam2 = 2 * d * unp.sin(theta2*(np.pi/180))
E3 = c * h /lam3
E2 = c * h /lam2

dE = E2 - E3

print("E2", E2, "E3", E3, "dE", dE)

sigma = z - unp.sqrt(4/alpha * unp.sqrt(dE/R) - (5* dE)/(R)) * unp.sqrt(1 + 19/32 * alpha**2 * dE/R)
print(sigma)