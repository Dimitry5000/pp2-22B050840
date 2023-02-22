def square(a,b):
    num = a
    while (num <= b):
        yield num * num
        num += 1
a = int(input())
b = int(input())
for i in square(a,b):
    print(i)
