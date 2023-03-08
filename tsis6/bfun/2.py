s = "dgsdNHGJkmfghgjHFGHj"
low = 0
up = 0
for i in s:
    if i.isupper():
        up += 1
    else:
        low += 1
print(low, up) 