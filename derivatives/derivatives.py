import math
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 3*x**2 + 2*x + 1

def df(x):
    return 6*x + 2


print(f(1))
print(df(1))

x = np.arange(-10, 10, 0.1)
y = f(x)

plt.plot(x, y)
plt.savefig('function_plot.png')  # Save plot before showing



