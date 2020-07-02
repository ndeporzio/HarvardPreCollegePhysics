import numpy as np
import matplotlib.pyplot as plt
import random

savepath='/Users/nicholasdeporzio/Desktop/'
n = 1000
t = 10
x=[0]*n
y=[0]*n
for i in range(n):
    r = random.gauss(np.sqrt(t), np.sqrt(t))
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

d = [[0]*n]*n
for i in range(n): 
    for j in range(n): 
        d[i][j] = np.sqrt(np.power(x[i]-x[j], 2.) + np.power(y[i]-y[j], 2.))

m = [0]*n
for i in range(n): 
    m[i] = np.mean(d[i])
    
        
plt.figure(figsize=(15,15))
plt.hist(m)
plt.xlabel(r"Mean Distance", fontsize=24)
plt.ylabel(r"Frequency", fontsize=24)
plt.grid(True, which='minor')
plt.savefig(savepath+'hist.png')
plt.show()
    


                     
    
    
