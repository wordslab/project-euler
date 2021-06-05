from Library import isSquare
from math import sqrt

s = 1000
for c in range(3, s):
    for b in range(3, c):
        A = (c-b)*(b+c) #difference of squares formula
        a = int(sqrt(A))
        if isSquare(A) and a < b and a+b+c == s: #checking all conditions
            print(str(a*b*c))
