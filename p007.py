from Library import isPrime
limit = 10001
count = 1
x = 1
while count < limit:
    x += 2 #checking only odd numbers
    if isPrime(x): #checking if prime
        count += 1
print(x)
