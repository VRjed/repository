c=0
d=0
for i in range(1213,8311):
    if i % 3 == 0 and i % 23 != 0:
        c += 1
        d += i
print(c,d)