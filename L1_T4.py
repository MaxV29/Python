%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 8, 61)
plt.plot(x, np.cos(x), marker="o")
print(x)
k = np.linspace(0, 21, 50)
plt.plot(k, np.cos(k), marker="o")
print(k)