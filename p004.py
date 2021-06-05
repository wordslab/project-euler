from Library import isPalindrome
def checkLast(n): #we need only numbers that can end with 9
    last = n % 10
    if (last == 1 or last == 3 or last == 9):
        return True
    else:
        return False

palindrome = 0
for i in range(901, 1000): #suffices to check integers above 900, the largest will be there
    if checkLast(i):
        for j in range(i, 1000):
            if checkLast(j):
                candidate = i * j
                if isPalindrome(str(candidate)) and palindrome < candidate:
                    palindrome = candidate
print(palindrome)
