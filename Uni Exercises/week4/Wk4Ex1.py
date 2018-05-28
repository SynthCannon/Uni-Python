# wk4ex1
# by Nicholas Sumner
# 25/10/12
# produces 2 2D graphs of cosx and sinx, e^x and e^-x

from pylab import *

#define window and format to be certain size and colour
fig=figure(figsize=(8,5), dpi=80)
fig.patch.set_facecolor('white')

#define length of X axis
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
#define each equation we shall be using
C,S,E,Q = np.cos(X), np.sin(X), np.exp(X), np.exp(-X)


subplot(2,1,1) #plot this on top
#format cosine and sine line plots
plot(X, C, color="blue", linewidth=1.5, linestyle="-", label="cosine") 
plot(X, S, color="red", linewidth=1.5, linestyle="-",  label="sine")

#define the axis of the graph
ax = gca()
#remove 'spines' set to table
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none') 
#set position relative to da
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
#set the ticks to the bottom on x axis and left on y axis
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

#give title to graph using the title function
title("Figure showing two subplot, with points labelled using LaTex text\n")

#set limits to the graph
xlim(X.min()*1.1, X.max()*1.1)
ylim(C.min()*1.1,C.max()*1.1)
#set defined ticks every pi/2 -pi to pi
xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
yticks([-1, +1],[r'$-1$', r'$+1$'])


t = 2*np.pi/3 #define t to be 2pi/3

#plot dotted line from cos to x axis at t=2pi/3
fig=plt.plot([t,t],[np.cos(t),0],
     color ='blue',  linewidth=1.5, linestyle="--")
#put blue point at cos(2pi/3)     
scatter([t,],[np.cos(t),], 50, color ='blue')
#annotate point with text in LaTex form
annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$', xy=(t, np.sin(t)),  xycoords='data',
         xytext=(+30, +5), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2")) #add arrow 

#plot dotted line from sin to x axis at t=2pi/3
plot([t,t],[0,np.sin(t)],
          color ='red',  linewidth=1.5, linestyle="--")
#put red point at sin(2pi/3          
scatter([t,],[np.sin(t),], 50, color ='red')
#annotate point with text in LaTex form
annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$', xy=(t, np.cos(t)),  xycoords='data',
         xytext=(-90, -50), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))


#put legend in the upper right corner
legend(loc='upper left')   
    
    
"""2nd PLOT"""

subplot(2,1,2) #plot this on bottom
#format exp(x) and exp(-x) line plots
plot(X, E, color="green", linewidth=1.5, linestyle="-", label="exp(x)") 
plot(X, Q, color="cyan", linewidth=1.5, linestyle="-",  label="exp(-x)")

#define the axis of the graph
ax2 = gca()
#remove 'spines' set to table
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
#set position relative to d
ax2.spines['bottom'].set_position(('data',0))
ax2.spines['left'].set_position(('data',0))
#set the ticks to the bottom on x axis and left on y axis
ax2.xaxis.set_ticks_position('bottom')
ax2.yaxis.set_ticks_position('left')

#set limits to the graph
xlim(X.min()*1.1, X.max()*1.1)
ylim(C.min()*1.1,C.max()*1.1)
#set defined ticks every pi/2 -pi to pi
xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
yticks([0, 10,+25],
       [r'$-1$', r'$+10$', r'$+exp(x)$'])

#put cyan point at (0,1)
scatter([0,],[1,], 35, color ='cyan')
#and annotate
annotate(r'$exp(0)=1$', xy=(0, 1),  xycoords='data',
         xytext=(40, 30), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
         
#put legend in the lower left corner    
legend(loc='lower left')

#change all tick text to size 10 and with no defining box
for label in ax.get_xticklabels() + ax.get_yticklabels() + ax2.get_xticklabels() + ax2.get_yticklabels() :
    label.set_fontsize(10)
    label.set_bbox(dict(facecolor='None', edgecolor='None', alpha=0.65 ))


#save the table produce
savefig("Y:/ph2150/Exercises/week4/exercice_10.png",dpi=72)
show()
