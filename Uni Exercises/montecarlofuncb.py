# An example montecarlo simulation for  a/x**2 fitting to data scaled to be 1 in the first bin of the histogram

from numpy import *
import matplotlib.pyplot as pl
from scipy.optimize import curve_fit
a=1.
def MyFunction(x,a): # defines the test function
    return a/x**2
start=0.1
end=10   
x= linspace(start,end,1000)
y= MyFunction(x,a)/MyFunction(start+0.005,a) #scaling the test function to equal 1 at the centre of the first bin in the histogram of simulated data
pl.plot(x,y)
n=10000 
z=zeros(n)
k=0
while k<n: # generates an array of n values where a value of x is appended to the array if condition is met
    px=random.rand(1)*end
    py = random.rand(1)*MyFunction(0.1,a)
    if py< MyFunction(px,a): # condition that point is added to array if random number < scaled function evaluated at x
        z[k]=px
        k+= 1
        #print k
                    
hist, bin_edges=histogram(z,1000,range=(start,end),density=True)# histogram sorts z into bins, density = True
#print hist
bin_middle=zeros(size(hist)) # histogram function returns bin edges, the next bit of code converts to bin middle
for n in range (0,len(hist)):
    bin_middle[n]=((bin_edges[n]+bin_edges[n+1])/2)
#scaledhist=hist/hist[0]


popt, pcov = curve_fit(MyFunction, bin_middle, hist)#curve fit to simulated data
scaledhist=hist/MyFunction(bin_middle[0],popt[0])
pl.plot(bin_middle,scaledhist)

pl.plot(bin_middle, MyFunction(bin_middle,popt[0])/MyFunction(bin_middle[0],popt[0]), label='best fit')
print popt * MyFunction(bin_middle[0],popt[0])
print pcov
pl.show()
