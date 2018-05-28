#b)
#math header file
import math
#constants
G=6.67*10**-11
M=5.97*10**24
R=6.371*10**6
#input
T=float(raw_input("what is the period of orbit of the satellite?: "))
#formula
h = math.pow(G*M*math.pow(T,2)/(2*math.pi)**2,0.3333333333333)-R
print 'the altitude is',h,'metres'
#c)
print 'the altitude the satellite would be at 45 min period is',math.pow(G*M*math.pow(45*60,2)/(2*math.pi)**2,0.3333333333333)-R
print 'the altitude the satellite would be at 90 min period is',math.pow(G*M*math.pow(90*60,2)/(2*math.pi)**2,0.3333333333333)-R
print 'the altitude a geosynchrous satellite takes is',math.pow(G*M*math.pow(24*60*60,2)/(2*math.pi)**2,0.3333333333333)-R