import re
pattern =  "[_]"
text = "sfa_sfa_af_fa"
x = re.split(pattern, text)
for i in x:
    print (i[0].upper(), i[1: len(i)], sep = "", end = "")