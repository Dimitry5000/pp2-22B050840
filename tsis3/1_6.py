def isprime(x):
    for i in range (2, int(x**(0.5)) + 1):
        if x % i == 0:
            return False
    return True
numbers = [1,2,3,4,5,6,7,8,9,10]
print (list(filter(isprime,numbers)))