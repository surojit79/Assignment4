import numpy as np
import scipy.stats

k=10 #no. of degrees of freedom
p_s=np.array([1/36,1/18,1/12,1/9,5/36,1/6,5/36,1/9,1/12,1/18,1/36])

#Case 1
Y1=np.array([4,10,10,13,20,18,18,11,13,14,13])
n1=np.sum(Y1)
V1=np.sum((Y1-n1*p_s)**2/(n1*p_s))
P1=1.0-scipy.stats.chi2.cdf(V1,k)  
print('for case 1:','V=',V1,'P(V>v)=',P1)

#Case 2
Y2=np.array([3,7,11,15,19,24,21,17,13,9,5])
n2=np.sum(Y2)
V2=np.sum((Y2-n2*p_s)**2/(n2*p_s))
P2=1.0-scipy.stats.chi2.cdf(V2,k)
print('for case 1:','V=',V2,'P(V>v)=',P2)

if((P1<0.01 or P1>0.99) and (P2<0.01 or P2>0.99)):
    print('not sufficient')
elif((0.01<P1<0.05 or 0.95<P1<0.99) and (0.01<P2<0.05 or 0.95<P2<0.99)):
    print('suspect')
elif((0.05<P1<0.1 or 0.9<P1<0.95) and (0.05<P2<0.1 or 0.9<P2<0.95)):
    print('almost suspect')   
elif((0.1<P1<0.9) and (0.1<P2<0.9)):
    print('sufficient')









