from pylab import *

figure(figsize=(8,5), dpi=80)

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S,E,Q = np.cos(X), np.sin(X), np.exp(X), np.exp(-X)

plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine") 
plot(X, S, color="red", linewidth=2.5, linestyle="-",  label="sine")