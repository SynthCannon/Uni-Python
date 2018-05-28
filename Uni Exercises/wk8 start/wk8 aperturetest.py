#PH2150
#Author: Andrew Casey
# Program to demonstrate the 2D FFT, fft2(),
#by calculating the diffraction pattern produced when 
#light passes through different shape/size apertures.

from pylab import *
import numpy as np
from scipy import *
import scipy.special
#from scipy.fftpack import fft2
import matplotlib.pyplot  as plt
from mayavi.mlab import surf

def circA(size): #Circular aperture 
    nx=256
    ny=256
    x=linspace(-20,20,nx)
    y=linspace(-20,20,ny)
    X,Y=meshgrid(x,y)
    r=np.sqrt(X**2+Y**2)
    A=np.zeros((nx,ny))
    for i in range(0,nx):
        for j in range(0,ny):
            if r[i,j] <= size:
                A[i,j]=1
            else:
                A[i,j]=0
    return(A)
    
def analyticCircA(): # Analytic result from the fft of circular aperture
    nx=256
    ny=256
    x=linspace(-20,20,nx)
    y=linspace(-20,20,ny)
    X,Y=meshgrid(x,y)
    z=np.sqrt(X**2+Y**2)
    I0=1
    f=I0*(2*scipy.special.j1(z)/z)**2
    A=np.zeros((nx,ny))
    for i in range(0,nx):
        for j in range(0,ny):
            A[i,j]=f[i,j]
    return(A)
    
    

def GuassianA(size): #Gaussian Aperture Function
    nx=256
    ny=256
    x=linspace(-20,20,nx)
    y=linspace(-20,20,ny)
    X,Y=meshgrid(x,y)
    r=np.sqrt(X**2+Y**2)
    rr=np.exp(-(X**2 +Y**2))
    A=np.zeros((nx,ny))
    for i in range(0,nx):
        for j in range(0,ny):
            if r[i,j] <= size:
                A[i,j]=rr[i,j]
            else:
                A[i,j]=0
    return(A)


def RectA(size1,size2): #Rectangular Aperture Function
    nx=256
    ny=256
    x=linspace(-20,20,nx)
    y=linspace(-20,20,ny)
    X,Y=meshgrid(x,y)
    ax=abs(X)
    ay=abs(Y)
    A=np.zeros((nx,ny))
    for i in range(0,nx):
        for j in range(0,ny):
            if ax[i,j] <= size1 and ay[i,j] <=size2:
                A[i,j]=1
            else:
                A[i,j]=0
    return(A)

# Setting up a grid for the plots
fig = plt.figure()

ax1 = plt.subplot2grid((3,3), (0,0))
ax2 = plt.subplot2grid((3,3), (0,1))
ax3 = plt.subplot2grid((3,3), (1, 0))
ax4 = plt.subplot2grid((3,3), (1, 1))
ax5 = plt.subplot2grid((3,3), (2, 0))
ax6 = plt.subplot2grid((3,3), (2, 1))
ax7 = plt.subplot2grid((3,3), (0, 2))
#Plot titles
ax1.set_title('Circular Aperture')
ax2.set_title('2D FFT of Circular Aperture')
ax3.set_title('Rectangular Aperture')
ax4.set_title('2D FFT of Rectangular Aperture')
ax5.set_title('Gaussian Aperture')
ax6.set_title('2D FFT of Gaussian Aperture')
ax7.set_title('Analyitic Solution to Circular')

#A=RectA(2,1)
 
A=circA(1)
ax1.imshow(A, cmap=cm.spectral)
Y = fft2(A)**2 # Evaluating 2D fft, then conveting to PSD
ax2.imshow(np.abs(fftshift(Y)), cmap=cm.spectral) # 2D plot of fft, fftshift moves zero-frequency component to the centre of the spectrum
B=RectA(1,0.5)
ax3.imshow(B, cmap=cm.spectral)
Z = fft2(B)**2
ax4.imshow(np.abs(fftshift(Z)), cmap=cm.spectral)
C=GuassianA(2)
ax5.imshow(C, cmap=cm.spectral)
ZZ = fft2(C)**2
ax6.imshow(np.abs(fftshift(ZZ)), cmap=cm.spectral)
AC=analyticCircA()
ax7.imshow(AC, cmap=cm.spectral)

plt.tight_layout() # A command to tidy up subplots
show()
