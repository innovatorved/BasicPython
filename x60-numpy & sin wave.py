import numpy as np
import matplotlib.pyplot as plt

x=np.arange(3,3*np.pi,0.4)

y=np.tan(x)
print(x)
print(y)

plt.plot(x,y)

plt.show()


