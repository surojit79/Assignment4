import numpy as np
import matplotlib.pyplot as plt

def f(x):
    if(3<x<7):
        return 1
    else:
        return 0

nsteps=10000
theta=0
X1=[]
X2=[]

for i in range(nsteps):
    theta_prime=theta+np.random.standard_normal()
    X1.append(theta_prime)
    r=np.random.rand()
    if(f(theta)!=0.0):
        if((f(theta_prime)/f(theta))>r):
            theta=theta_prime
    else:
        theta=theta_prime
    X2.append(theta)

#Markov chain
step=np.linspace(1,nsteps,nsteps)
plt.plot(step,X1,'r',label=r'all points')
plt.plot(step,X2,'g',label=r'Markov chain')
plt.xlabel('step')
plt.ylabel('X')
plt.title('Markov Chain')
plt.legend()
plt.show()

Y1=np.linspace(3,7,11)
Y2=np.ones(11)*0.25

# pdf
plt.hist(X2,range=(2,8),bins=20,density=True,label=r'Histogram')
plt.plot(Y1,Y2,lw=3,color='b',label=r'uniform pdf')
plt.xlabel("X")
plt.ylabel("PDF")
plt.title("Density plot")
plt.legend()
plt.show()





