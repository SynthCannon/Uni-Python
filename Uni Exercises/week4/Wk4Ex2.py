# wk4ex2
# by Nicholas Sumner
# 25/10/12
# Produces 3d graph from stm.dat

import numpy as np
from mayavi import mlab

f=open("stm.dat","r")

#put all data into an array, reads the array then splits it into a list and reshaped to array
a=np.array([float(n) for n in f.read().split()]).reshape(384,384)
    
mlab.surf(a) #3d reconstruction technique, rendors faster than sift
mlab.show()
