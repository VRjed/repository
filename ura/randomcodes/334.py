a = 53**123 + 65**2222 - 172**12 
print(a)
b = ''
alf = '0123456789№#@$*'
while a != 0:
    b += str(a%7)
    a = a //7
b = b[::-1]
h = 0
for j in range(1,6):
    h += b.count('6' + str(j))
print(h)