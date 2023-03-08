a = ord("A")
for i in range (a, a+26):
    f = open(chr(i) + ".txt", "x")
    f.close()