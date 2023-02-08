import math as m
import random as r
def grtoounce(gr):
    return (28.3495231*gr)
def frtoc(fr):
    print((5/9)*(fr-32))
def solve(numheads, numlegs):
    print ("Number of chickens:" , (4*numheads - numlegs)/2)
    print ("Number of rabbits:" , (numlegs - 2* numheads)/2)
def isprime(x):
    for i in range (2, int(x**(0.5)) + 1):
        if x % i == 0:
            return False
    return True
def retprime(x):
    return list(filter(isprime, x))
def revsen(st):
    s = ""
    while st.find(" "):
        s += st[st.find(" "):]
        st = st[:st.find(" ")]
    s += " " + st
    return s
def three(x):
    for i in range(1,len(x)):
        if x[i] == 3:
            if x[i-1] == 3:
                return True
    return False
def three2(x):
    for i in range(2,len(x)):
        if x[i] == 7:
            if x[i-1] == 0:
                if x[i-2] == 0:
                    return True
    return False
def vol(x):
    return((4/3)*m.pi*x*x*x)
def un(x):
    r = []
    for i in x:
        if i in r:
            pass
        else:
            r.append(i)
    return r
def pal(x):
    for i in range (len(x)//2 + 1):
        if x[i] != x[-(i+1)]:
            return False
    return True
def histogram(x):
    for i in range (len(x)):
        print ("*"*x[i])
def guess():
    name = input("Hello! What is your name?")
    cnt = 0
    num = r.randint(1,20)
    print ("Well,", name , ", I am thinking of a number between 1 and 20.")
    while True:
        n = int(input("Take a guess"))
        cnt += 1
        if n == num:
            print ("Good job,", name , "! You guessed my number in", cnt, "guesses!")
            break
        if n > num:
            print ("Your guess is to high")
        else:
            print("Your guess is too low")
