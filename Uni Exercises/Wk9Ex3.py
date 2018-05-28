from numpy import *
from pylab import *
from mpl_toolkits.mplot3d import Axes3D 
from mayavi.mlab import quiver3d, show

#Dimensions of the box
a = 0.36
b = 0.33
d = 0.23

x,y,z = mgrid[0.:0.36:0.01, 0.:0.33:0.01, 0:0.23:0.01]

def omega(mx,my,mz): # does not include v term, divide by v to get omega
    return (mx**2 + (my * a / b)**2 + (mz * a / d)**2)**(1./2.)
    
for k in range (0,3):
    for j in range (0,3):
        for i in range (0,3):
            print "i:", i,"j:", j,"k:", k, omega(i,j,k)

def kx(m):
    return (m * pi / a)
def ky(n):
    return (n * pi / b)
def kz(l):
    return (l * pi / d)
def k(n,m,l):
    return np.sqrt(kx(n)**2 * ky(m)**2 * kz(l)**2)
    
def Ex(x,y,z,n,m,l):
    return np.cos(kx(n) * x) * np.sin(ky(m) * y) * np.sin(kz(l) * z)
def Ey(x,y,z,n,m,l):
    return - kx(n) / ky(m) * np.sin(kx(n) * x) * np.cos(ky(m) * y) * np.sin(kz(l) * z)
def Ez(x,y,z,n,m,l):
    return z*0
    
def Bx(x,y,z,n,m,l):
    return - ky(m)/k(n,m,l) * np.sin(kx(n) * x) * np.cos(ky(m) * y) * np.cos(kz(l) * z)
def By(x,y,z,n,m,l):
    return kx(n)/k(n,m,l) * np.cos(kx(n) * x) * np.sin(ky(m) * y) * np.cos(kz(l) * z)
def Bz(x,y,z,n,m,l):
    return z*0
    

ex1=Ex(x,y,z,0,1,1)
ey1=Ey(x,y,z,0,1,1)
ez1=Ez(x,y,z,0,1,1)

ex2=Ex(x,y,z,1,1,1)
ey2=Ey(x,y,z,1,1,1)
ez2=Ez(x,y,z,1,1,1)

bx1=Bx(x,y,z,0,1,1)
by1=By(x,y,z,0,1,1)
bz1=Bz(x,y,z,0,1,1)

bx2=Bx(x,y,z,1,1,1)
by2=By(x,y,z,1,1,1)
bz2=Bz(x,y,z,1,1,1)

quiver3d(x,y,z,ex1,ey1,ez1)
show()
quiver3d(x,y,z,ex2,ey2,ez2)
show()
quiver3d(x,y,z,bx1,by1,bz1)
show()
quiver3d(x,y,z,bx2,by2,bz2)
show()
