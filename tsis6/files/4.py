fname = "anyfile.txt"
f = open(fname, "r")
x = f.readlines()
print(len(x))
f.close()
