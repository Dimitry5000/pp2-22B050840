def sqgen(n):
    num = 0
    while (num <= n):
        yield num * num
        num += 1
n = 5
for i in sqgen(n):
    print(i, end=" ")
