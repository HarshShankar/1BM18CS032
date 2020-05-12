import random as rm
import numpy as np
import matplotlib.pyplot as plt
import time
from sklearn import linear_model as lr

def recursiveLinearSearch(arr, ele, i):
    if i == len(arr):
        # print("Element not found")
        return

    if arr[i] == ele:
        # print("Element found at " + str(i))
        return
    else:
        return recursiveLinearSearch(arr, ele, i+1)
ranges = 10
yplot = []
xplot = []
while(ranges <= 1000):
    arr = [rm.randint(0, ranges) for _ in range(0, ranges, 1)]
    ele = arr[len(arr)-1]
    st1 = time.process_time()
    recursiveLinearSearch(arr, ele, 0)
    tt = time.process_time() - st1
    yplot.append(tt)
    xplot.append(ranges)
    ranges = ranges + 50

xp1 = np.array(xplot)
yp1 = np.array(yplot)
reg1 = lr.LinearRegression()
reg1.fit(xp1.reshape(-1, 1), yplot)
plt.plot(xp1, reg1.predict(xp1.reshape(-1, 1)), color="blue")
plt.scatter(xp1, yp1, color="red", marker="+")
plt.show()
