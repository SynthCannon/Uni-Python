import numpy as np
import matplotlib.pyplot as plt
import itertools

def func(x):
    if x >= 1.0 or x <= -1.0:
        return 0
    else:
        return (abs(x) - 1.0)

a = 1.
b = -1.
N = 99.
time = np.linspace( a, b, N )
y = (np.fromiter(itertools.imap(func, time), 
                  dtype=time.dtype, count=time.shape[0]))

period = 2.
def cn(n):
    c = y*np.exp(-1j*2*n*np.pi*time/period)
    return c.sum()/c.size

def f(x, Nh):
    rng = np.arange(.5, Nh+.5)
    f = np.array([2*cn(i)*np.exp(2j*i*np.pi*x/period) for i in rng])
    return f.sum()

y2 = np.array([f(t,10).real for t in time])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(time, y)
ax.plot(time, y2)
plt.show() 
