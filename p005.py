n = 20
i = 1
for j in range(1, n+1):
    if i % j != 0: #checking if divisible
        for k in range (1, n+1):
            if (i*k) % j == 0: #if not divisible, need to know what to multiply by to make divisible
                i *= k
                break
print(i)
