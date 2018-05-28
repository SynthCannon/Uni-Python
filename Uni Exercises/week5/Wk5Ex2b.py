# wk5ex2b
# by Nicholas Sumner
# 1/11/12
# produces graph of sine wave with error bars

import numpy as np
from scipy.optimize import curve_fit
from pylab import *
import matplotlib.pyplot as plt

def sinFit(x,a,b):
    return a*np.sin(b*x)

#open and put data file into x and y lists
(x, y) = loadtxt('Y:/ph2150/Exercises/week5/fitting_week5.dat').transpose()
#use curvefit to consider uncertainty
popt, pcov = curve_fit(sinFit,x,y)
print "parameters:\na=",popt[0],"b=",popt[1]
print "covariance: ",pcov

#define the plot
fig=plt.figure()
plt.scatter(x,y,label="data",lw=2)
plt.plot(x,sinFit(x,popt[0],popt[1]),label="best fit",lw=1)
plt.legend()
plt.show()
