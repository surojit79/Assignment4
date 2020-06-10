import numpy as np
import matplotlib.pyplot as plt

x=np.random.rand(10000)
plt.hist(x,range=(0.0,1.0),density=True)
plt.show()
