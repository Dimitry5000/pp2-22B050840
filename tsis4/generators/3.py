def divgen(n):
    num = 0
    while (num <= n):
        if (num % 3 == 0 or num % 4 == 0):
            yield num
        num += 1
n = int(input())
for i in divgen(n):
    print(i)
