from pylab import *
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def func(x, m, c):
    return m*x+c # function to generate data for curvefit

file1=np.loadtxt('data.dat')
(x,y,xerr,yerr)=np.array(file1.transpose())

file2=np.loadtxt('data2.dat')
(x2,y2,xerr2,yerr2)=np.array(file2.transpose())
popt2, pcov2 = curve_fit(func, x2, y2)

file2=np.loadtxt('data3.dat')
(x3,y3,xerr3,yerr3)=np.array(file2.transpose())
popt3, pcov3 = curve_fit(func, x3, y3)

#define window and format to be certain size and colour
fig=figure(figsize=(16,16), dpi=50)
fig.patch.set_facecolor('white')

ax = fig.add_subplot(221)
ax.scatter(x, y, color="blue", s=1, edgecolor='none',label="Data")
ax.errorbar(x,y,yerr=yerr,xerr=xerr)
#set position of spines:
#ax.spines['bottom'].set_position(('data',0))
#ax.spines['left'].set_position(('data',0))
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.grid(True,linestyle='-',color='green')

#set limits of axis
xlim(0, 300)
ylim(0, 800)
#set defined ticks 
#xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
#yticks([-1, +1],[r'$-1$', r'$+1$'])
#set title and axis names
ax.set_title("Inverse Magnetic Susceptibility as a function of Temperature",fontsize=13)
ax.set_xlabel("Temperature (K)",fontsize=12)
ax.set_ylabel("Inverse Magnetic Susceptibility (cgs)",fontsize=12)
#ax.legend()


ax2 = fig.add_subplot(222)
ax2.scatter(x, y, s=1, color='red', label="Data2")
ax2.errorbar(x,y,yerr=yerr,xerr=xerr)
#set position of spines:
#ax2.spines['bottom'].set_position(('data',0))
#ax2.spines['left'].set_position(('data',0))
ax2.xaxis.set_ticks_position('bottom')
ax2.yaxis.set_ticks_position('left')
ax2.grid(True,linestyle='-',color='green')
ax2.annotate('Counter-Curie-Weiss\nLaw Descrepency', xy=(13., 51.5),  xycoords='data',
         xytext=(-10, 40), textcoords='offset points', fontsize=11,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.1"))
#set limits of axis
xlim(0, 300)
ylim(0, 800)
#set defined ticks 
#xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
#yticks([-1, +1],[r'$-1$', r'$+1$'])
#set title and axis names
ax2.set_title("Inverse Magnetic Susceptibility as a function of Temperature\nThe Change of Phase",fontsize=13)
ax2.set_xlabel("Temperature (K)",fontsize=12)
ax2.set_ylabel("Inverse Magnetic Susceptibility (cgs)",fontsize=12)
#ax2.legend()


ax3 = fig.add_subplot(223)
ax3.scatter(x2, y2, color="blue", s=1, edgecolor='none',label="Data")
ax3.errorbar(x2,y2,yerr=yerr2,xerr=xerr2)
#set position of spines:
#ax3.spines['bottom'].set_position(('data',0))
#ax3.spines['left'].set_position(('data',0))
ax3.xaxis.set_ticks_position('bottom')
ax3.yaxis.set_ticks_position('left')
ax3.grid(True,linestyle='-',color='green')
#set limits of axis
xlim(0, 300)
ylim(0, 800)
#set defined ticks 
#xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
#yticks([-1, +1],[r'$-1$', r'$+1$'])
#set title and axis names
ax3.set_title("Inverse Magnetic Susceptibility as a function of Temperature",fontsize=13)
ax3.set_xlabel("Temperature (K)",fontsize=12)
ax3.set_ylabel("Inverse Magnetic Susceptibility (cgs)",fontsize=12)
#ax3.legend()


ax4 = fig.add_subplot(224)
ax4.scatter(x3, y3, color="blue", s=1, edgecolor='none',label="Data")
ax4.errorbar(x3,y3,yerr=yerr3,xerr=xerr3)
def lineofbestfit(x):
    return x*popt3[0]+popt3[1]
    
x=linspace(0,300,1024)
ax4.plot(x,lineofbestfit(x))
#set position of spines:
#ax4.spines['bottom'].set_position(('data',0))
#ax4.spines['left'].set_position(('data',0))
ax4.xaxis.set_ticks_position('bottom')
ax4.yaxis.set_ticks_position('left')
ax4.grid(True,linestyle='-',color='green')
#set limits of axis
xlim(0, 300)
ylim(0, 80)
#set defined ticks 
#xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
#yticks([-1, +1],[r'$-1$', r'$+1$'])
#set title and axis names
ax4.set_title("Inverse Magnetic Susceptibility as a function of Temperature\nLine of Best Fit",fontsize=13)
ax4.set_xlabel("Temperature (K)",fontsize=12)
ax4.set_ylabel("Inverse Magnetic Susceptibility (SI)",fontsize=12)
#ax4.legend()


#print popt[0],popt[1]
print popt3[0],popt3[1]

#fig.subplots_adjust(hspace=.5,wspace=.5)
show()