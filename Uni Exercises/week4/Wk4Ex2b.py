# wk4ex2b
# by Nicholas Sumner
# 25/10/12
# converting image of phantoms to single channel

from matplotlib.pylab import *
from math import *
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

#define window features
fig=figure(figsize=(8,5), dpi=80)
fig.patch.set_facecolor('white')#background

#add 1st graphic to interface
fig.add_subplot(2,1,1)
#imports NMR_Phantom as an array.
img = mpimg.imread('NMR_Phantom.png')
#displays the array "img" as an image.
imgplot = plt.imshow(img)                   

#slice the array to a single channel (from greyscale to RBG color) 
lum_img = img[:,:,0]    

#add 2nd graphic (image with 
fig.add_subplot(2,1,2)
plt.colorbar() 
imgplot2 = plt.imshow(lum_img)              

show() 
savefig("Y:/ph2150/Exercises/week4/exercice_3.png",dpi=72)
