from cmath import log
import matplotlib.pyplot as plt
import math

x = [i for i in range(-1001, 1001)]
y = [i**90 for i in range(-1001, 1001)]

# print(x)
# print(y)
plt.plot(x, y)
plt.show()