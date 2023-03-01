import re
pattern =  "[.\s,]"
text = "sfa.bm,b   bbfdsf"
x = re.sub(pattern, ":", text)
print(x)