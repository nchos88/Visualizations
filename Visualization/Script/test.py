import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10 , 10 , 0.1)

y = 1.0/(1.0+np.exp(x - 2))

plt.plot(x,y)
plt.show()
