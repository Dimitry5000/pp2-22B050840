import re
pattern =  "[A-Z]"
text = "sfa_sfa_af_fa"
x = re.split(pattern, text)
print (x)