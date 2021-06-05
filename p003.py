pf = 2
x = 600851475143
while pf < x:
    if x % pf == 0: #checking divisibility
        x /= pf
    else:
        pf += 1 #if not divisible, checking next number
print(pf)
