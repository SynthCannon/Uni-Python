# wk5ex1
# by Nicholas Sumner
# 1/11/12
# produces 2 fourier series graphs

import numpy as np
from pylab import *
import itertools
#import time
#import sys

#define the window and set the back colour white
fig = figure()
fig.patch.set_facecolor('white')

#define an array of 256 values between 0 to 2pi
x = np.linspace(0., 2*np.pi, 256,endpoint=True)

#this function produces a square wave function
def func(x2,N):
    limit=np.arange(1.,N+1.)
    f = np.sum([2*np.sin((n*x2))*(1-(-1)**n)/(n*np.pi) for n in limit])
    return f

#this function produces a saw tooth function
def func2(x3,N):
    limit=np.arange(1.,N+1.)
    f2=np.pi/2+np.sum([(-1-(-1)**n)*np.sin(n*x3)/n for n in limit])
    return f2
	

#add and annotate table1 for square wave
ax = fig.add_subplot(2,1,1)
ax.plot(x,[func(X,999) for X in x],color="red", linewidth=1., linestyle="-", label="N=999")#add red line for N=999 terms
ax.plot(x,[func(X,99) for X in x],color="green", linewidth=0.6, linestyle="-", label="N=99")#add green line for N=99 terms
ax.plot(x,[func(X,9) for X in x],color="blue", linewidth=0.6, linestyle="-", label="N=9")#add blue line for N=9 terms
xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],[r'$0$', r'$\pi/2$', r'$+\pi$', r'$+3\pi/2$', r'$+2\pi$']) #put x range from 0 to 2pi
yticks([-1.5, 0, +1.5],[r'$-1.5$', r'$0$', r'$+1.5$']) #put y range from -1.5 to +1.5 
legend(loc='upper right') 

#add and annotate table2 for sawtooth wave
ax2 = fig.add_subplot(2,1,2)
ax2.plot(x,[func2(X,999) for X in x],color="red", linewidth=1., linestyle="-", label="N=999")#add red line for N=999 terms
ax2.plot(x,[func2(X,99) for X in x],color="green", linewidth=0.6, linestyle="-", label="N=99")#add green line for N=99 terms
ax2.plot(x,[func2(X,9) for X in x],color="blue", linewidth=0.6, linestyle="-", label="N=9")#add blue line for N=9 terms
xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],[r'$0$', r'$\pi/2$', r'$+\pi$', r'$+3\pi/2$', r'$+2\pi$']) #put x range from 0 to 2pi
yticks([0, +np.pi],[r'$0$', r'$+\pi$']) #put y range from 0 to +pi
legend(loc='lower right') 

show()
"""fig2=figure()
ax3=fig2.add_subplot(1,1,1)
n=1
line, =plot(func(x,n), animated=True)
draw()
def callback(*args):
    line.set_ydata(x,n+1)
    ax3.draw_animated()"""




