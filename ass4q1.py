import numpy as np
import matplotlib.pyplot as plt

m=2**31
a=1103515245
c=12345
x=1

n=10000
result=[]

for i in range(n):
    x=(a*x+c)%m
    result.append(x/(m))
    

plt.hist(result, density = True)
plt.show()
