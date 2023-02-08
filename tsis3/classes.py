import math as m
class Cstring():
    def __init__ (self):
        self.stringc = ""
    def getstring(self):
        x = int(input())
        self.stringc = x
    def printString(self,x):
        print (self.stringc.upper())
class Shape():
    def __init__ (self):
        self.area = 0
    def printarea(self):
        print (self.area)
class Square(Shape):
    def __init__(self,length):
        self.length = length
class Rectangle(Shape):
    def __init__ (self, length, width):
        self.length = length
        self.width = width
    def computearea(self):
        self.area = self.length * self.width
class Point():
    def __init__ (self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print (self.x, self.y)
    def move(self,x,y):
        self.x = x
        self.y = y
    def dist(self, p):
        dist = m.sqrt((self.x - p.x)*(self.x - p.x) + (self.y - p.y) * (self.y - p.y))
        return dist
class Account():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,s):
        self.balance += s
    def withdraw(self,s):
        if s <= self.balance:
            self.balance -= s
        else :
            print("There is not enough money in the account to withdraw")

