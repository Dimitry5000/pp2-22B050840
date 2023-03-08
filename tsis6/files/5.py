fname = "anyfile.txt"
f = open(fname, "w")
x = [1,2,3,4,5,6]
for i in x:
    f.write(str(i))
    f.write(" ")
f.close()
