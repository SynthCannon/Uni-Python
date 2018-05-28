from pylab import *
from Tkinter import * 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import rc
import numpy as np
import tkMessageBox #output only in the form of a popup
import tkSimpleDialog #lets the user input a string
import tkFileDialog
from scipy import *
from scipy.optimize import curve_fit
from sympy import pretty_print as pp, latex


"""
to do list:
    add monte carlo method
    add potential to load data
    add help section
    error handle
"""


a = 1.*10**27
r = 1.*10**-6
            
        
e = 1.6021766*10**-19 # charge of an electron in Coulombs  = 1.602 176 565 35 * 10^-19 C
eps_0 = 8.8541878* 10**12  #epsilon_0, electrical constant = 8.854 187 817 620 * 10^-12 F.m^-1 (Farads per metre)



elements = ['Hydrogen Z=1',
            'Helium Z=2',
            'Lithium Z=3',
            'Beryllium Z=4',
            'Boron Z=5',
            'Carbon Z=6',
            'Nitrogen Z=7',
            'Oxygen Z=8',
            'Fluorin Z=9',
            'Neon Z=10',
            'Sodium Z=11',
            'Magnesium Z=12',
            'Aluminium Z=13',
            'Silicon Z=14',
            'Phosphorus Z=15',
            'Sulfur Z=16',
            'Chlorine Z=17',
            'Argon Z=18',
            'Potassium Z=19',
            'Calcium Z=20',
            'Scandium Z=21',
            'Titanium Z=22',
            'Vanadium Z=23',
            'Chromium Z=24',
            'Manganese Z=25',
            'Iron Z=26',
            'Cobalt Z=27',
            'Nickel Z=28',
            'Copper Z=29',
            'Zinc Z=30',
            'Gallium Z=31',
            'Germanium Z=32',
            'Arsenic Z=33',
            'Selenium Z=34',
            'Bromine Z=35',
            'Krypton Z=36',
            'Rubidium Z=37',
            'Strontium Z=38',
            'Yttrium Z=39',
            'Zirconium Z=40',
            'Niobium Z=41',
            'Molybdenum Z=42',
            'Technetium Z=43',
            'Ruthenium Z=44',
            'Rhodium Z=45',
            'Palladium Z=46',
            'Silver Z=47',
            'Cadmium Z=48',
            'Indium Z=49',
            'Tin Z=50',
            'Antimony Z=51',
            'Tellurium Z=52',
            'Iodine Z=53',
            'Xenon Z=54',
            'Caesium Z=55',
            'Barium Z=56',
            'Lanthanum Z=57',
            'Cerium Z=58',
            'Praseodymium Z=59',
            'Neodymium Z=60',
            'Promethium Z=61',
            'Samarium Z=62',
            'Europium Z=63',
            'Gadolinium Z=64',
            'Terbium Z=65',
            'Dysprosium Z=66',
            'Holmium Z=67',
            'Erbium Z=68',
            'Thulium Z=69',
            'Ytterbium Z=70',
            'Lutetium Z=71',
            'Hafnium Z=72',
            'Tantalum Z=73',
            'Tungsten Z=74',
            'Rhenium Z=75',
            'Osmium Z=76',
            'Iridium Z=77',
            'Platinum Z=78',
            'Gold Z=79',
            'Mercury Z=80',
            'Thallium Z=81',
            'Lead Z=82',
            'Bismuth Z=83',
            'Polonium Z=84',
            'Astatine Z=85',
            'Radon Z=86',
            'Francium Z=87',
            'Radium Z=88',
            'Actinium Z=89',
            'Thorium Z=90',
            'Protactinium Z=91',
            'Uranium Z=92',
            'Neptunium Z=93',
            'Plutonium Z=94',
            'Americium Z=95',
            'Curium Z=96',
            'Berkelium Z=97',
            'Californium Z=98',
            'Einsteinium Z=99',
            'Fermium Z=100',
            'Mendelevium Z=101',
            'Nobelium Z=102',
            'Lawrencium Z=103',
            'Rutherfordium Z=104',
            'Dubnium Z=105',
            'Seaborgium Z=106',
            'Bohrium Z=107',
            'Hassium Z=108',
            'Meitnerium Z=109',
            'Darmstadtium Z=110',
            'Roentgenium Z=111',
            'Ununbium Z=112',
            'Ununtrium Z=113',
            'Ununquadium Z=114',
            'Ununpentium Z=115',
            'Ununhexium Z=116',
            'Ununseptium Z=117',
            'Ununoctium Z=118']    
    
    

class RutherfordGUI:
    def __init__(self, master):
        #create a container
        frame = Frame(master)
        #this puts all the frames as close together as possible, a bit like the tight_layout command
        frame.pack()
        #makes a canvas widget that will show the final calculation
        self.addInputs(frame,master)
        self.addPlot(frame)
	
    def addInputs(self,frame,master):
        #builds the frame which will hold all the inputs and their labels
        InputFrame = Frame(frame)
        #places this frame at co-ord (0,0) of the master frame
        InputFrame.grid(column = 0, row = 0)
        
        #the labels:
        self.lbln = Label(InputFrame, text = "N: ", justify=LEFT)
        self.lbln.grid(column= 0,row= 1)
        self.lbln = Label(InputFrame, text = "t: ", justify=LEFT)
        self.lbln.grid(column= 0,row= 2)
        self.lbln = Label(InputFrame, text = r"E$_{k}$: ", justify=LEFT)#put in latex format
        self.lbln.grid(column= 0,row= 3)
        
        #Entry Boxes
        self.N_entry = Entry(InputFrame)
        self.N_entry.grid(column = 1, row = 1)
        self.t_entry = Entry(InputFrame)
        self.t_entry.grid(column = 1, row = 2)
        self.EK_entry = Entry(InputFrame)
        self.EK_entry.grid(column = 1, row = 3)
        
        #Buttons
        self.butPlot = Button(InputFrame, text ='Plot', command = self.calcInputs)
        self.butPlot.grid(column = 1, row = 4)
        self.butMonteCarlo = Button(InputFrame, text ='Monte Carlo Simulation', command = self.MonteCarlo)
        self.butMonteCarlo.grid(column = 1, row = 5)
        self.butImport = Button(InputFrame, text ='Import', command = self.importData)
        self.butImport.grid(column = 1, row = 6)
        
        
        #Dropbox of elements
        self.dropOpt = StringVar()
        self.dropOpt.set(elements[78])
        self.Z_dropbox= OptionMenu(InputFrame, self.dropOpt, *elements)
        self.Z_dropbox.grid(column = 1, row = 0)
        
        frame.pack()
        
    def addPlot(self, frame):
        self.fig = Figure(figsize=(6,4), dpi=100) #makes a figure object
        self.fig.patch.set_facecolor('white')
        self.figPlot = self.fig.add_subplot(111) #adds a plot to that figure
        
        
        self.canvas = FigureCanvasTkAgg(self.fig,frame) #adds the figure to the container
        self.canvas.get_tk_widget().grid(row = 0, column = 1) #gives the figure a location (compulsary)
        
        #adds a standard plot toolbar
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, frame) 
        self.toolbar.update()
        self.toolbar.grid(row = 7, column = 1)
        
        self.canvas.show()
        frame.pack()
        
    
    def RutherfordScattering(self,phi,N,t,EK,Z):
        p1 = (N*a*t)/(16*r**2)
        p2 = (2 * Z * e**2) /(4*pi*eps_0*EK)**2
        
        if np.sin(phi/2.)!=0:
            n = p1*p2/(np.sin(phi/2.))**4
        return n
        

    def RutherfordScattering2(self,phi,C):
        error,N,t,EK,Z = self.GetInputs()
        if error == False:
            p1 = (N*a*t)/(16*r**2)
            p2 = (2 * Z * e**2) /(4*pi*eps_0*EK)**2
        
            n = np.log(C*p1*p2/(np.sin(phi/2.))**4)
            
            return n


    def option(self):
        x=0
        for i in elements:
            if  i == self.dropOpt.get():
                return x
            x=x+1
            
    def calcInputs(self):
        error,N,t,EK,Z = self.GetInputs()
        if error == False:
            Phi = linspace(0.02,pi-0.2/1000.,1000)
            counts = np.array([self.RutherfordScattering(phi,N,t,EK,Z) for phi in Phi])
            self.figPlot.plot(Phi,counts)
            self.canvas.show()     
            
    def MonteCarlo(self):
        error,N,t,EK,Z = self.GetInputs()
        k=0
        if error == False:
            z=zeros(10000)
            while k<10000:
                rx=random.rand(1)*pi
                ry = random.rand(1)*self.RutherfordScattering(pi-0.2/1000.,N,t,EK,Z)
                if ry< self.RutherfordScattering(rx,N,t,EK,Z): # condition that point is added to array if random number < scaled function evaluated at x
                    z[k]=rx
                    k+= 1
            hist, bin_edges=histogram(z,1000,range=(0.02,pi),density=True)
            print hist
            bin_middle=zeros(size(hist))
            for n in range (0,len(hist)):
                bin_middle[n]=((bin_edges[n]+bin_edges[n+1])/2)
            
    
            #popt,pcov = curve_fit(self.RutherfordScattering2, bin_middle, hist)
            
            #scaledhist=hist/self.RutherfordScattering2(bin_middle[0],popt[0])
            #self.figPlot.plot(bin_middle, self.RutherfordScattering(bin_middle,popt[0])/self.RutherfordScattering(bin_middle[0],popt[0]))
		

        print 'o'
        
    def importData(self):
        print 'lol'
        
	
    def GetInputs(self):
        Z = float(self.option())
        err_bool=False
        if Z==0:
            tkMessageBox.showinfo("Error!", "Please choose a value for Z")
            err_bool = True
        else:
            try:
                N=int(self.N_entry.get())
            except:
                tkMessageBox.showinfo("Error!", "N has to be an integer")
                err_bool = True
            try:
                t = float(self.t_entry.get())
            except:
                tkMessageBox.showinfo("Error!", "t has to be a float")
                err_bool = True
            try:
                EK =float(self.EK_entry.get())
            except:
                tkMessageBox.showinfo("Error!", "E_k has to be a float")
                err_bool = True
        return err_bool,N,t,EK,Z
		


    
        

#define root
root=Tk()
root.wm_title("Ruthorford Scattering Application")
RutherfordGUI(root)
#run the main loop
root.mainloop()