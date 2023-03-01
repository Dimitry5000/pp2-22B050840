import re
j = 0
pattern =  "[A-Z]"
text = "AfabsfiBbfanAfbon"
x = re.findall(pattern, text)
y = re.split(pattern, text)
print (x)
y.remove("")
for i in range (len(y)):
    print (x[i], y[i], sep = "", end = " ")

