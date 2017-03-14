import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
import sys
import csv
import pylab

f = open(sys.argv[1], 'rt')
A=[]
Z=[]
try:
    reader = csv.reader(f)
    for row in reader:
        A.append(float(row[0]))
        Z.append(float(row[6]))
        print(A)
finally:
    f.close()

plt.scatter(A, Z)
plt.title('Atomic Mass vs. Mean Free Path')
plt.xlabel('Atomic masses')
plt.ylabel('Mean Free Path (barns^-1)')
plt.ylim(0,.2)
plt.xlim(0,240)
plt.show()
