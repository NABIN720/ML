# percentile
import numpy as np

# x = [12,13,154,43,33,66,55,77,88,54,55,51,52,43,44,49,48]

# y= np.percentile(x,90)
# print(y)

# DATA DISTRIBUTION
import matplotlib.pyplot as plt
# x = np.random.uniform(0.0,5.0,250)
# plt.hist(x,5)
# plt.show()

# array of 100000 random nujmbers
# x = np.random.uniform(0.0,5.0,100000)
# plt.hist(x,100)
# plt.show()

# NORMAL DISTRIBUTION

# x = np.random.normal(5.0,1.0,100000)
# plt.hist(x,100)
# plt.show()

# SCATTER PLOT
# x = [5,7,8,4,6,9,3,10,11,12,13,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# plt.scatter(x,y)
# plt.show()

# A SCATTER PLOT WITH 1000 DOTS

x = np.random.normal(5.0,1.0,1000)
y = np.random.normal(7.0,2.0,1000)

# plt.scatter(x,y)
# plt.show()
x = np.random.normal(loc=1, scale=2, size=5)
y = np.random.normal(loc=3, scale=4, size=5)
print(x,y)
plt.scatter(x,y)
plt.show()