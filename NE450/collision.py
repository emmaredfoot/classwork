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
        Z.append(float(row[2]))
        print(A)
finally:
    f.close()

plt.scatter(A, Z)
plt.title('Atomic Mass versus Average Neutron Collisions [25 MeV - .025MeV]')
plt.xlabel('Atomic masses')
plt.ylabel('Average number of Collsions Neutron')
plt.ylim(0,900)
plt.xlim(0,250)
plt.show()
