sum = 0
for x in range(1,1000):
    if x % 3 == 0 or x % 5 == 0: #checking if 0 mod 3 or 0 mod 5
        sum += x #adding to sum
print(sum)
