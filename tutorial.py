import random 
import numpy as np
import matplotlib.pyplot as plt

savepath='/Users/nicholasdeporzio/Desktop/'
n = 1000
t = 10000
x=[0]*n
y=[0]*n
for i in range(n):
    r = random.gauss(np.sqrt(t), np.sqrt(t)/4)
    theta = random.random()*2.*np.pi
    x[i] = r*np.cos(theta)
    y[i] = r*np.sin(theta)
    
plt.figure(figsize=(15,15))
plt.scatter(x, y)
plt.xlabel(r"X", fontsize=24)
plt.ylabel(r"Y", fontsize=24)
plt.grid(True, which='minor')
plt.savefig(savepath+'data.png')
plt.show()

l = np.zeros(n)
for i in range(n): 
    l[i] = np.sqrt(np.power(x[i], 2.) + np.power(y[i], 2.))
plt.figure(figsize=(15,15))
plt.hist(l)
plt.xlabel(r"Distance From Origin", fontsize=24)
plt.ylabel(r"Frequency", fontsize=24)
plt.grid(True, which='minor')
plt.savefig(savepath+'hist1.png')
plt.show()

d = np.zeros((n,n))
for j in range(n): 
    for i in range(n):
        d[i,j] = np.sqrt(np.power(x[i]-x[j], 2.) + np.power(y[i]-y[j], 2.))
        
plt.figure(figsize=(15,15))
plt.hist(d[20])
plt.xlabel(r"Distance from Other Particles", fontsize=24)
plt.ylabel(r"Frequency", fontsize=24)
plt.grid(True, which='minor')
plt.savefig(savepath+'hist2.png')
plt.show()

m = np.zeros(n)

for i in range(n): 
    m[i] = np.mean(d[i, :])
             
plt.figure(figsize=(15,15))
plt.hist(m)
plt.xlabel(r"Mean Distance from Other Particles", fontsize=24)
plt.ylabel(r"Frequency", fontsize=24)
plt.grid(True, which='minor')
plt.savefig(savepath+'hist3.png')
plt.show()
