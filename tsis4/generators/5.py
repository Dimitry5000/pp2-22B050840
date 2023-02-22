def dgen(n):
    num = n
    while (num > 0):
        yield num
        num -= 1
n = 5
for i in dgen(n):
    print(i)
