a = 5*216**1256 - 5*36**1146 + 4*6**1053 - 1087 
b = ''
alf = '0123456789№#@$*'
while a != 0:
    b += str(a%6)
    a = a //6
b = b[::-1]
h = 0
for j in b:
    h += int(j)
print(h)