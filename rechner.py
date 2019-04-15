import numpy as np 
import math
import pandas as pd
from uncertainties import ufloat
from uncertainties import unumpy as unp
#import matplotlib.pyplot as plt
#from scipy.optimize import curve_fit


R = 13.6
alpha = 7.297e-3
z = [35, 30, 38, 40]
#E = [13474, 9659, 16105, 17998]
E = [13288.97525493,  9507.64602919, 15186.81014756, 16435.42826949]
konst = np.zeros(4)
i = 0
while i < 4:
    konst[i] = z[i] - np.sqrt(z[i]**2 + ( E[i] - R * z[i]**2)/R )
    i = i +1
print(konst)    

j = 0
theta = [13.4, 18.9, 11.2, 10.8]
lam = np.zeros(4)
K = np.zeros(4)
c=3*10**8
h=4.135*10**(-15)
d=201.4*10**(-12)
while j < 4:
    lam[j] = 2 * d * np.sin(theta[j]*(np.pi/180))
    K[j] = c * h /lam[j]
    j = j+1

print(K)