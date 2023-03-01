import re
pattern =  r".*ab{2,3}[^b]+"
text = "sfabbbbfdsf"
print (re.search(pattern, text))