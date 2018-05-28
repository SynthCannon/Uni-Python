##Nicholas Sumner 
##11/10/12
##Wk2Ex2:

#Header Files
import math

#Ex2a: Function to find a triangles area from coordinates
def TriangleArea(list):
    area1=0.5*abs(list[0]*list[3]+list[2]*list[5]+list[4]*list[1]-list[0]*list[5]-list[2]*list[1]-list[4]*list[3])#area=1/2(x1*y2+x2*y3+x3*y1-x1*y3-x2*y1-x3*y2)
    return area1

#Ex2b: Function to find length of path
def pathlength(a1,b1,a2,b2,prevlength):
    Len=prevlength+math.sqrt((a2-a1)**2+(b2-b1)**2) #length = pythagorus of previous coordinates
    return Len
    
#Ex2c: outputting circle data to user
def pi_approx(len):
    print 'circumference is: ',len
    a=len/math.pi*100
    print 'Percentage out of pi is ',"%.2f" % a

##Main Program:
length=0
option=raw_input('This is week 2 exercise 2\ndo you want part a, b or c?: ')
if(option=='a'):
    print 'Part a'
    #input coordinates
    areaCoordinates=(float(raw_input("x1: ")),float(raw_input("y1: ")),float(raw_input("x2: ")),float(raw_input("y2: ")),float(raw_input("x3: ")),float(raw_input("y3: ")))
    print 'The area of the triangle is: ',TriangleArea(areaCoordinates)
#end option a
    
if(option=='b'):
    print 'Part b\nHere you start off at some coordinates and increase the\nlength of the path by going to new coordinates\n'
    initialX=float(raw_input("Starting x coordinate: "))
    initialY=float(raw_input("Starting y coordinate: "))
    
    while(option!='n'): #for inputting more values
        option='b' #default, needed as option changes
        
        finalX=float(raw_input("New x coordinate: "))
        finalY=float(raw_input("New y coordinate: "))
        
        length=pathlength(initialX,initialY,finalX,finalY,length)
        print 'The length of the path you have covered is: ',length
        
        #ask if user wants to put in more coordinates
        while(option!='n')and(option!='y'):#while not a valid option
            option=raw_input("want to put in more coordinates? y/n\n")
            if (option!='n') and (option!='y'): #validation, reject if not y or n
                print 'please try another input\n'
        
        #set final coordinates as initial coordinates
        initialX=finalX 
        initialY=finalY
#end option b

if(option=='c'):
    #initializing
    length=0
    i=0
    k=2
    initialX2=0
    initialY2=0
    print 'Part c\n'
    
    
    while(k<10):
        length=0
        i=0
        while(i!=2**k):
            #pass parameters to the path length
            length=pathlength(initialX2,initialY2,0.5*math.cos(2*math.pi*i/2**k),0.5*math.sin(2*math.pi*i/2**k),length)
            #redifine initial values
            initialX2=0.5*math.cos(2*math.pi*i/2**k)
            initialY2=0.5*math.sin(2*math.pi*i/2**k)
            i+=1
            
        k+=1
        print 'For k=',k,pi_approx(length)
#end option c