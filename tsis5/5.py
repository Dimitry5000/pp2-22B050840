import re
pattern =  "a.*b$"
text = "sfabbbbfdsfb"
print (re.search(pattern, text))