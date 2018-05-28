# wk5ex1
# by 
# 1/11/12
# 
import numpy as np
from pylab import *
import itertools

#
fig = figure()
fig.patch.set_facecolor('white')
#
x = np.linspace(0., 2*np.pi, 256,endpoint=True)

#
def func(x2,N):
    limit=np.arange(1.,N+1.)
    f = np.sum([2*np.sin((n*x2))*(1-(-1)**n)/(n*np.pi) for n in limit])
    return f

#
def func2(x3,N):
    limit=np.arange(1.,N+1.)
    f2=np.pi/2+np.sum([(-1-(-1)**n)*np.sin(n*x3)/n for n in limit])
    return f2
	

#
ax = fig.add_subplot(2,1,1)
ax.plot(x,[func(X,999) for X in x],color="red", linewidth=1., linestyle="-")
ax.plot(x,[func(X,99) for X in x],color="green", linewidth=0.6, linestyle="-")
ax.plot(x,[func(X,9) for X in x],color="blue", linewidth=0.6, linestyle="-")
xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],[r'$0$', r'$\pi/2$', r'$+\pi$', r'$+3\pi/2$', r'$+2\pi$']) #put x range from 0 to 2pi
yticks([-1.5, 0, +1.5],[r'$-1.5$', r'$0$', r'$+1.5$']) #put y range from -1.5 to +1.5 

#
ax2 = fig.add_subplot(2,1,2)
ax2.plot(x,[func2(X,999) for X in x],color="red", linewidth=1., linestyle="-")
ax2.plot(x,[func2(X,99) for X in x],color="green", linewidth=0.6, linestyle="-")
ax2.plot(x,[func2(X,9) for X in x],color="blue", linewidth=0.6, linestyle="-")
xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],[r'$0$', r'$\pi/2$', r'$+\pi$', r'$+3\pi/2$', r'$+2\pi$']) #put x range from 0 to 2pi
yticks([0, +np.pi],[r'$0$', r'$+\pi$']) #put y range from 0 to +pi
show()
