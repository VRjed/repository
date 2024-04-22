a = 103*7**103-5*7**57+98
b = ''
alf = '0123456789№#@$*'
while a != 0:
    b += str(a%7)
    a = a //7
b = b[::-1]
h = 0
for j in b:
    h += int(j)
print(h)