import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer

start_time1=timer()             

m=2**31
a=1103515245
c=12345
x=1

n=10000
result=[]

for i in range(n):
    x=(a*x+c)%m
    result.append(x/(m))

end_time1=timer() 
print('time taken for LCG =',end_time1-start_time1)

start_time2=timer()
 
x=np.random.rand(10000)

end_time2=timer() 

print('time taken using numpy =',end_time2-start_time2)


