#Wk3Ex4 
#by Nicholas Sumner
import pylab
from Tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
from mayavi.mlab import surf

#make it cheap and shit!

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




class ApertureMain:
    def __init__(self, master):
        #constructs the frame which will hold all the other widgets
        frame = Frame(master)
        #this puts all the frames as close together as possible, a bit like the tight_layout command
        frame.pack()
        #calls functions which build the 2 main program areas
        self.makePlot(frame)#,d1=0,d2=0)
        self.makeInputs(frame)
        self.v=3
        
    def makePlot(self, frame):
        #makes a canvas widget that will show the final calculation
        self.fig = Figure(figsize=(6,4), dpi=100) #makes a figure object
        #This line is the important bit. you cant just embed a figure into a tkinter front end
        #The Canvas object can deal with loads of things but here we are going to make it
        #with our figure object embeded into it        
        self.canvas = FigureCanvasTkAgg(self.fig,frame)
        self.canvas.show()
        #the get_tk_widget.grid places it at co-ord (0,1) of the master frame 
        self.canvas.get_tk_widget().grid(row = 0, column = 1)
        #adds a standard plot toolbar
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, frame)
        self.toolbar.update()
        self.toolbar.grid(row = 7, column = 1)
        
    def makeInputs(self, frame):
        #builds the frame which will hold all the inputs and their labels
        InputFrame = Frame(frame)
        #places this frame at co-ord (0,0) of the master frame
        InputFrame.grid(column = 0, row = 0)
        
        #Radio Buttons
        v=3
        self.radio_R = Radiobutton(InputFrame, text="Rectangular", variable=v, value=0)
        self.radio_C = Radiobutton(InputFrame, text="Circular", variable=v, value=1)
        self.radio_G = Radiobutton(InputFrame, text="Gaussian", variable=v, value=2)
        print v
        
        self.radio_R.grid(column = 0, row = 0)
        self.radio_C.grid(column = 0, row = 1)
        self.radio_G.grid(column = 0, row = 2)
        
        """self.radio_R.deselect()
        self.radio_C.deselect()
        self.radio_G.deselect()"""
        
        #the labels
        self.lbl1 = Label(InputFrame, text = "x distance:", justify=LEFT)
        self.lbl1.grid(column= 0,row= 3)
        self.lbl2 = Label(InputFrame, text = "y distance:", justify=LEFT)
        self.lbl2.grid(column= 0,row= 4)
        
        #Entry Boxes
        self.ent1 = Entry(InputFrame)
        self.ent1.grid(column = 1, row = 3)
        self.ent2 = Entry(InputFrame)
        self.ent2.grid(column = 1, row = 4)
        
        #lets put a plot button in to refresh which we probably wont need to use
        self.butPlot = Button(InputFrame, text ='PLOT', command=self.mapNewPlot(InputFrame))
        self.butPlot.grid(column = 0, row = 9)
        
    #def deselectRadios(self,mode):
     #   print "ifhe"
    
    def mapNewPlot(self,frame):
        if v<3:
            d1 = float(self.ent1.get())#.get returns a string from that object
            d2 = float(self.ent2.get())
            if v==0:
                A=rectA(1)
                ax.imshow(A, cmap=cm.spectral)
            else if v==1:
                A=circA(1)
                ax.imshow(A, cmap=cm.spectral)
            else if v==2:
                A=gaussianA(1)
                ax.imshow(A, cmap=cm.spectral)
            show()
                
            
            #self.canvas.show() 
        if v==3:
            self.radio_R.deselect()
            self.radio_C.deselect()
            self.radio_G.deselect()
            v=0
        
        
        
#make me a tk object    
root = Tk()
aperture = ApertureMain(root)
#run the main loop
root.mainloop()