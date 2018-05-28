##Nicholas Sumner 
##11/10/12
##Wk2Ex3:

#Header Files
import math

def gauss(x,m,s):
    G=1.0/(math.sqrt(2*math.pi*s))*math.exp(((-0.5)*(x-m))**2)
    return G
    
#Main Program
for x in range(-5,6):
    gauss(x,0,1)