fname = "anyfile.txt"
fname2 = "anyfile2.txt"
f = open(fname, "r")
f2 = open(fname2, "w")
f2.write(f.read())
f.close()
f2.close()