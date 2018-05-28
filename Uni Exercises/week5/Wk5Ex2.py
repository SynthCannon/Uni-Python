# wk5ex2a
# by Nicholas Sumner
# 1/11/12
# produces y equal to a*e^-(b*x) with error bars 
#from a random generator

import numpy as np
from scipy.optimize import curve_fit
from pylab import *
import matplotlib.pyplot as plt

def func(x, a, b, c):
    return a*np.exp(-b*x) + c # function to generate data for curvefit
x = np.linspace(0, 4, 50)
y = func(x,  2.5, 1.3, 0.5)
yn = y + 0.2*np.random.normal(size=len(x)) #adding some noise to the data points
#define the error on y (new)

yerr=np.sqrt(np.abs(yn-y))
popt, pcov = curve_fit(func, x, yn)
print ' Parameters : ' , popt
print ' Covariance : ' , pcov
popt, pcov = curve_fit(func, x, yn, sigma=yerr) # performing curvefit and returning parameters
print ' Parameters : ' , popt
print ' Covariance : ' , pcov

#graphical output of results
fig=plt.figure()
plt.scatter(x, y, label='data')
#plot the errors
plt.errorbar(x,yn,yerr=yerr,label="data + noise")
plt.plot(x, yn, label='data + noise')
plt.plot(x, func(x, popt[0], popt[1], popt[2]), label='bestfit')
plt.legend()
plt.show()

""" without yerr:
Parameters :  [ 2.37584369  1.26183201  0.54877326]
Covariance :  [[ 0.01721209  0.00702399 -0.00102661]
[ 0.00702399  0.02371121  0.00691145]
[-0.00102661  0.00691145  0.00364004]]
with yerr:
Parameters :  [ 2.43107273  1.24473871  0.5034772 ]
Covariance :  [[0.00555225  0.0016149  -0.000377]
[ 0.0016149   0.00722978  0.00208386]
[-0.000377    0.00208386  0.00104413]]

the function curve fit with noise values passed into it will produce better results closer to the true value
"""

