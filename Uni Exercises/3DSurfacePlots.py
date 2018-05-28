from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

# Author: Tim Lehner
# Example code to show some 3D surface plots, with nice additions

# Define functions
def sinc(x):
    return 10 / np.pi * np.sin((np.pi) * 1/10. * x) / x
    
def cos(x):
    return np.sin((np.pi) * 1/40. * x)
    
# These functions, combined, will create a 3D surface that is
# difficult to immediately see. In order to make the graph 
# clearer, projections on the X and Y Plane will reveal the
# functions used to create the 3d surface.


# Set up the 3D drawing space
fig = plt.figure()
ax = fig.gca(projection='3d')

# Set up X,Y meshgrid using meshgrid(xRange,yRange) where xRange, yRange are 1D arrays
X, Y = np.meshgrid(np.linspace(-40,40,num=100), np.linspace(-40,40,num=100))

Z = sinc(X) * cos(Y)

# Plot the surface
ax.plot_surface(X, Y, Z, rstride=8, cstride=8, cmap=cm.coolwarm, alpha=0.3)

# Project onto x, y planes
cset = ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
cset = ax.contourf(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)

# add a labeled colour bar
cbar = fig.colorbar(cset)
cbar.set_label("Intensity")

# labels, limits, titles
ax.set_xlabel('X Label')
ax.set_xlim(-40, 40)
ax.set_ylabel('Y Label')
ax.set_ylim(-40, 40)
ax.set_zlabel('Z Zabel')
ax.set_zlim(-1, 1)

plt.title("Surface example")

plt.show()

print Z
