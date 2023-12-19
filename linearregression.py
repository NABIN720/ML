# regression is used when you try to find the relationship between variables
#  in ml and statistical modeling, that relationship is used to predict the outcomes of future events

# uses the relationship between the data-points to draw a straight line through all them.

import matplotlib.pyplot as plt
from scipy import stats

x = [5, 7, 8, 4, 6, 9, 3, 10, 11, 12, 13, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = stats.linregress(x,y)
print(slope)
print(intercept)
print(r)
print(p)
print(std_err)


def myfunc(x):

    return slope*x + intercept

mymodel = list(map(myfunc,x))


plt.scatter(x,y)
plt.plot(x,mymodel)
plt.show()