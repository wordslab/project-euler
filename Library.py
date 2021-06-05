from math import sqrt
def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    else:
        for div in range(3, int(sqrt(n)) + 1, 2):
            if n % div == 0:
                return False
    return True

def countDiv(n):
    count = 2
    if isPrime(n):
        return count
    for div in range(2, int(sqrt(n)) + 1):
        if n % div == 0 and not n / div == div:
            count += 2
        elif n / div == div:
            count += 1
        else:
            continue
    return count

def isSquare(n):
    check = sqrt(n) - int(sqrt(n))
    if check != 0:
        return False
    else:
        return True

def isPalindrome(s):
    return s == s[::-1]

def digitSum(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    return sum

def digitLen(n):
    s = str(n)
    return len(s)
