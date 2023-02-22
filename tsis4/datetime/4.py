import datetime
def calcdif(x , y):
    sec1 = x.year * 365 * 24 * 60 * 60 + x.month * 30 * 24 * 60 * 60 + x.day * 24 * 60 * 60 + x.hour * 60 * 60 + x.minute * 60 + x.second
    sec2 = y.year * 365 * 24 * 60 * 60 + y.month * 30 * 24 * 60 * 60 + y.day * 24 * 60 * 60 + y.hour * 60 * 60 + y.minute * 60 + y.second
    return sec1 - sec2
x = datetime.datetime.now()
y = datetime.datetime(2022, 2 , 21 , 14 , 43, 4)
print(calcdif(x,y))