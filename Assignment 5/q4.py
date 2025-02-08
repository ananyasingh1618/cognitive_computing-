import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 100)
y1 = x ** 2
y2 = np.sin(x)
y3 = np.exp(x)
y4 = np.log(np.abs(x) + 1)
plt.plot(x, y1, label="y = x^2")
plt.plot(x, y2, label="y = sin(x)")
plt.plot(x, y3, label="y = exp(x)")
plt.plot(x, y4, label="y = log(|x| + 1)")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Function Plots")
plt.legend()
plt.grid()
plt.show()
