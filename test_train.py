import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2)

x = np.random.normal(3, 1, 100)
print(x)
y = np.random.normal(150, 40, 100)/ x
print(y)

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

plt.scatter(x,y)
plt.show()