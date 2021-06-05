x1 = 0
x2 = 2
sum = 0
while x2 < 4000000: #upper bound of 4 million
    sum += x2
    t = (4*x2) + x1 #derived recurrence for even Fibonacci numbers
    x1 = x2
    x2 = t
print(sum)
