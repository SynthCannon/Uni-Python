
from pylab import *
from scipy.integrate import quad

fig=figure(figsize=(8,5), dpi=80)
fig.patch.set_facecolor('white')

#



#wavefunction for single particle
#phi_n(x) = (2/L)^0.5 * sin(n*pi*x/L)
#i have set L equal to one in order to intergrate numerically
def wavefunc( x , n ): 
    return np.sqrt(2)*np.sin(n*np.pi*x)

#define an array of 256 values between 0 to 1 for the plot
xlimits = np.linspace(0., 1., 256,endpoint=True)


plot(xlimits, [wavefunc(X,3) for X in xlimits], color="blue", linewidth=1.5, linestyle="-", label="phi 3") 
plot(xlimits, [wavefunc(X,4) for X in xlimits], color="red", linewidth=1.5, linestyle="-",  label="phi 4")
plot(xlimits, [wavefunc(X,3)*wavefunc(X,4) for X in xlimits], color="green", linewidth=1.5, linestyle="-",  label="phi 3x4")    

#this function defines the formula inside the orthogonality relation
def wavefunc2(x,n,m):
    return 2*np.sin(n*np.pi*x)*np.sin(m*np.pi*x)
    
#show()
iprod, err = quad(wavefunc2, 0 , 1 ,args=(3,4) )
print "integrating the orthogonality relation for x from 0 to L gives", iprod
print "this has an error of", err, "which is",err/iprod,"times bigger than the value obtained from the integral"
print "therefore it is safe to assume that the integral is equal to 0"

#test the orthogonality relation for 4 different values:
iprod1,errorbuff= quad(wavefunc2, 0 , 1 ,args=(1,1) )
print iprod1
iprod2,errorbuff= quad(wavefunc2, 0 , 1 ,args=(2,2) )
print iprod2
iprod3,errorbuff= quad(wavefunc2, 0 , 1 ,args=(2,3) )
print iprod3
iprod4,errorbuff= quad(wavefunc2, 0 , 1 ,args=(3,4) )
print iprod4

#
#this function defines the formula inside the expectation value function
def wavefunc3(x,n):
    return 2*np.sin(n*np.pi*x)*x*np.sin(n*np.pi*x)

#the expectation value is given by the integral of phi*_n * x * phi_n
iprod5,errorbuff= quad(wavefunc3, 0 , 1 ,args=(4) )
iprod6,errorbuff= quad(wavefunc3, 0 , 1 ,args=(7) )
iprod7,errorbuff= quad(wavefunc3, 0 , 1 ,args=(9) )
print iprod5,iprod6,iprod7

#this function defines the formula inside the square expectation value function
def wavefunc4(x,n):
    return 2*np.sin(n*np.pi*x)*x**2*np.sin(n*np.pi*x)


iprod5,errorbuff= quad(wavefunc4, 0 , 1 ,args=(4) )
iprod6,errorbuff= quad(wavefunc4, 0 , 1 ,args=(7) )
iprod7,errorbuff= quad(wavefunc4, 0 , 1 ,args=(100) )
print iprod5,iprod6,iprod7

    



