# Wk8ex2
# by Nicholas Sumner
#22/11/12
import matplotlib.pyplot as plt
from numpy import linspace
import pylab

"""
The class Gravity's initializer will set each instance
the mass of both objects for newtons law of gravitation as m and M 
alongside the gravitational constant.
the force method returns the value of the force and the visualize
method produces a Force vs Distance graph of the 2 objects.
"""

class Gravity:
    """Gravity force between two physical objects."""
    def __init__(self, m, M):
        self.m = m # mass of object 1
        self.M = M # mass of object 2
        self.G = 6.67428E-11 # gravitational constant , m**3/kg/s**2
    def force(self,r):
        G, m, M = self.G, self.m, self.M
        return G*m*M/r**2
    def visualize(self, r_start, r_stop, n=100, Electric = False):
        """
        r_start and r_stop - defines the boundaries of distance
        from point source you want to plot then makes an array out
        of it defined r
        overall this will plot a graph of distance to force
        """
        r = linspace(r_start, r_stop, n) 
        g = self.force(r) # set g as force for values of each value in r
        plt.plot(r,g) #plot r vs g with title
        if Electric == True:
            plt.title('Electric force: q1=%g C, q2=%g C' %(self.m, self.M))
        else: 
            plt.title('Gravity force: m=%g, M=%g' %(self.m, self.M))
        plt.xlabel('r m**2')
        plt.ylabel('Force kg*m*s**-2')
        plt.show()
        

"""
Define the ElectricForce as a subclass of gravity as they are both
inverse square laws with different parameters:
-m and M are now supposedly the charges of each object
-redefine G to be the Coulomb field constant
Now our subclass will inherit the same methods as superclass Gravity 
with minimal coding
"""

class ElectricForce(Gravity):
    def __init__(self, m, M):
        Gravity.__init__(self, m , M )
        self.G=8.99E9 # Coulomb constant , kg * m**3 / A**2 / s**4
        
    
charge1=float(raw_input("Charge on charge 1:"))
charge2=float(raw_input("Charge on charge 2:"))

#define an instance for ElectricForce
inst=ElectricForce(charge1,charge2)

Rstart=float(raw_input("Lower displacement boundary:"))
Rstop=float(raw_input("Upper displacement boundary:"))

if Rstart<Rstop:
    # Call visualize method from Gravity for instance of ElectricForce
    inst.visualize(Rstart,Rstop,n=100, Electric=True)
else:
    print "The starting distance must be less than the upper bound"
    