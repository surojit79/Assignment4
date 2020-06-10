import numpy as np
import matplotlib.pyplot as plt

x1=np.random.rand(10000)
x2=np.random.rand(10000)

y1=np.sqrt(-2*np.log(x1))*np.cos(2*np.pi*x2)
y2=np.sqrt(-2*np.log(x1))*np.sin(2*np.pi*x2)

plt.hist(y1,range=(-5.0,5.0),bins=20,density=True,label=r'Box-Muller')

x=np.linspace(-5,5,1000)
y=np.exp(-0.5*x**2)/np.sqrt(2*np.pi)
plt.plot(x,y,'r',label=r'Gaussian')
plt.xlabel("x")
plt.legend()
plt.show()



