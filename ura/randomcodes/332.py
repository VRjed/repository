a = 19**81+23**709-4
print(a)
b = ''
alf = '0123456789№#@$*'
while a != 0:
    b += str(a%9)
    a = a //9
b = b[::-1]
h = 0
for j in range(1,8):
    h += b.count('8' + str(j))
print(h)