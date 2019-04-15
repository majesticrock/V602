import numpy as np 
import math
import pandas as pd
from uncertainties import ufloat
from uncertainties import unumpy as unp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def func(x, a, b):
    return a*x + b

werte = csv_read("csv/messung.csv")
xdata = np.zeros(4)
ydata = np.zeros(4)

ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        xdata[i] = np.sqrt(float(values[2]))
        ydata[i] =  float(values[1]) 
        i+=1

x_line = np.linspace(30, 45)
plt.plot(xdata, ydata, "rx", label="Messdaten")
popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt), "b-", label="Fit")

print(popt)
print(pcov)

plt.xlabel(r"$\sqrt{E_{\symup{K}}} $ / $\sqrt{\symup{eV}}")
plt.ylabel(r"$Z$")
plt.legend()
plt.tight_layout()
plt.savefig("build/ekz.pdf")