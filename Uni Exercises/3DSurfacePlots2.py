from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

import os # for easy working dir

# Author: Tim Lehner
# Example code to show some 3D surface plots, with nice additions


# Set up the 3D drawing space
fig = plt.figure()
ax = fig.gca(projection='3d')

# Set up X,Y meshgrid using meshgrid(xRange,yRange) where xRange, yRange are 1D arrays
X, Y = np.meshgrid(np.linspace(0,100,num=101),np.linspace(0,1200,num=1201))

# Place zData in the same directory as this file, and marvel at the brilliance of loadtxt!
Z = np.loadtxt(os.path.dirname(os.path.realpath(__file__)) + '\\zData.txt')

Gx, Gy = np.gradient(Z)
N= (Gx**2+Gy**2)**.5 / ((Gx**2+Gy**2)**.5).max()
# Plot the surface
colour = 'jet'
cset=ax.plot_surface(X, Y, Z, rstride=100, cstride=10, cmap=colour, alpha=0.7)
ax.plot_surface(X, Y, Z, rstride=10, cstride=1, alpha=0.7,linewidth=0, facecolors=cm.jet(N))#, antialiased=False, shade=False)

# Project onto x, y planes
#cset = ax.contourf(X, Y, Z, zdir='x', offset=00, cmap=colour)
#cset = ax.contourf(X, Y, Z, zdir='z', offset=np.min(Z), cmap=colour)

# add a labeled colour bar
cbar = fig.colorbar(cset)
cbar.set_label("Intensity")

# labels, limits, titles
ax.set_xlabel('X Label')
ax.set_xlim(0, 100)
ax.set_ylabel('Y Label')
ax.set_ylim(0, 1200)
ax.set_zlabel('Z Zabel')
ax.set_zlim(np.min(Z), np.max(Z))

plt.title("Surface example")

plt.show()

#"""