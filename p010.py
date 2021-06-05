from Library import isPrime
sum = 2
for i in range(3, 2000001, 2):
    if isPrime(i): #adding primes to sum
        sum += i
print(sum)
