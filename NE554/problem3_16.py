#Emma Redfoot
#NE554
#Problem 3.16
import sys
import csv
from scipy.stats import chisquare

f = open(sys.argv[1], 'rt')
A=[]
try:
    reader = csv.reader(f)
    for row in reader:
        A.append(float(row[0]))
        print(A)
finally:
    f.close()

print(chisquare(A))
