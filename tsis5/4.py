import re
pattern =  "[A-Z][a-z]+"
text = "Asfabbbbfdsf"
print (re.search(pattern, text))