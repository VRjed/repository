a = 81**18 - (81**8 - 1)*((8 + 1)**8 + 1)// 8 - 8
print(a)
b = ''
alf = '0123456789№#@$*'
while a != 0:
    b += str(a%3)
    a = a //3
b = b[::-1]
h = 0
#for j in b:
    #h += int(j)
print(b.count('1'))