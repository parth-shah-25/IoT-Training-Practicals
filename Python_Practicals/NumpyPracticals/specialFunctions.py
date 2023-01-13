import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3*np.pi,0.1)
# y = np.sin(x) # Plots Sine Graph
# y = np.cos(x) # Plots Cosine Graph
y = np.tan(x) # Plots tangent Graph
plt.plot(x,y)
# plt.show()

a = np.array([1,2,3])

print(np.exp(a)) # Exponential
print("Natural Log:\n",np.log(a)) # Logarithmic (Natural)
print("Log Base 10:\n",np.log10(a)) # Logarithmic (Log Base 10)
