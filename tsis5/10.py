import re
s = ""
pattern =  "[A-Z]"
text = "AfabsfiBbfanAfbon"
x = re.findall(pattern, text)
y = re.split(pattern, text)
print (x)
y.remove("")
for i in range (len(y)):
    s += x[i].lower() + y[i] + "_"
print (s[:-1])

