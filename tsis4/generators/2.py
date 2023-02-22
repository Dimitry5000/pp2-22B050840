def evgen(n):
    num = 0
    while (num <= (n - n%2) / 2):
        yield num * 2
        num += 1
n = int(input())
for i in evgen(n):
    print(i, end = ",")
