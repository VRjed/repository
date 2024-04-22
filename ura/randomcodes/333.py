a = 81**79+75**2022-12**35
print(a)
b = ''
alf = '0123456789№#@$*'
while a != 0:
    b += str(a%5)
    a = a //5
b = b[::-1]
h = 0
for j in range(1,4):
    h += b.count('4' + str(j))
print(h)