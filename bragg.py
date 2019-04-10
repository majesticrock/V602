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
#theta = 4.7 *np.pi/180 
#theta = 22.5 *np.pi/180
theta = 20.29 *np.pi/180

E = h * c / (2 * d * np.sin(theta))
print(E)
E = 0.2
l = h *c / E
E = 0.83
print(l)