import numpy as np
import matplotlib.pyplot as plt

def f(x):
      return(np.sqrt(2/np.pi)*np.exp(-0.5*x**2))
def g(x):
      return (1.5*np.exp(-x))

x=np.random.rand(100000)
x=-np.log(x)
y=np.random.rand(100000)*g(x)

y_good=[]
x_good=[]

y_good=y[y < f(x)]
x_good=x[y < f(x)]

z=np.linspace(0,10,1000)

plt.hist(x_good,range=(0.0,10.0),bins=20,density=True,label=r'Rejection')
plt.plot(z,f(z),'r',label=r'erf')
plt.xlabel("x")
plt.legend()
plt.show()

