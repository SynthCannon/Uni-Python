#wk8ex1
#By Nicholas Sumner
import matplotlib.pyplot as plt
from numpy import linspace
from pylab import *
"""
A fluid that flows through a (very long) pipe has zero 
velocity on the pipe wall and a maximum velocity 
along the centerline of the pipe.
"""
class VelocityProfile:
	"""
	plot v versus r
	"""
	def __init__(self):
        #set some initializers for the fluid flow equation
		self.R=1 #
		self.beta=0.06 
		self.mu0=0.02 
		self.n=0.1
	def fluid_flow(self,r):
        """
        The formula for fluid flow is given by
        v(r) = [(beta / 2*mu_0)**(-1/n)] * [n/(n+1)] * [R**(1+1/n) - r**(1+1/n)]
		The square brackets indicate how I have broken this code up
        for readability purposes.
        """
        a = (self.beta / (2. * self.mu0)) ** (1. / self.n)  # (beta / 2*mu_0)**(-1/n)
		b = self.n / (self.n+1)                             # n/(n+1)
		c = self.R**(1+1/self.n) - r**(1+1/self.n)        # R**(1+1/n) - r**(1+1/n)
		v=a*b*c
		return v
	def plot_table(self):
        """
        standard plotting procedure:
        define 1D array of numbers for r (metres)
        send array to fluid_flow eqn, returns v(r) for each value
        and puts into the 1D array velocity. Plots, then shows.
        """
		r=linspace(-self.R,self.R,100)
		velocity=self.fluid_flow(r)
		plt.plot(r,velocity)
		plt.show()
        
#define an instance of VelocityProfile
inst=VelocityProfile()
#use method plot_table
inst.plot_table()
		
		
