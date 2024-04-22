a = 4*25**4 - 5**4 + 14
b = ''
while a != 0:
    b += str(a%5)
    a = a //5
b = b[::-1]
h = 0
for j in b:
    h += int(j)
print(h)