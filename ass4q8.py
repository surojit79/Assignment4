import numpy as np
def f(r):
    return(np.sum(r*r))

dim=np.array([[2],[10]])
n=100000
V=np.zeros(2)
for i in range(2):
    d=dim[i]

 
    count=0
    for j in range(n):
    
        r=np.random.uniform(-1,1,d)
        if (f(r)<=1.0):
            count=count+1
    x=(count/n)*2**d
    V[i]=x
print('Area of the 2d unit circle=',V[0])
print('Volume of the 10d unit circle=',V[1])



    





