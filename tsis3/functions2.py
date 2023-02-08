def film(x,i):
    if x[i].get("imdb") >= 5.5:
        return True
    return False
def list(x):
    r = []
    for i in x:
        if i.get("imdb") >= 5.5:
            r.append(i)
    return r
def cat(x,c):
    r = []
    for i in x:
        if i.get("category") == c:
            r.append(i)
    return r
def avg(x):
    sum = 0
    cnt = 0
    for i in x:
        cnt += 1
        sum += i.get("imdb")
    return sum/cnt
def avgcat(x,c):
    catmov = cat(x,c)
    return avg(catmov)
