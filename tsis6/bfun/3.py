s = "abcdgsgsdghfcvvvba"
for i in range (len(s)):
    if s[i] == s[len(s) - i - 1]:
        pass
    else:
        print("No")
        break
else:
    print ("Yes")