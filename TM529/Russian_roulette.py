import numpy as np
import matplotlib.pyplot as plt
import sys
import csv
import pylab


A=[1,2,3,4,5,6,5,4,3,2,1]
Z=[y / 36 for y in A]
X=[2,3,4,5,6,7,8,9,10,11,12]
print(Z)

width = 1/1.5
plt.bar(X, Z, width, color="blue")
plt.title('Probability of Rolling each value')
plt.xlabel('Value of Each Roll')
plt.ylabel('Probability')
plt.show()
