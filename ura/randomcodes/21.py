a = 18**105 + 25*16**100 - 3**51 +15**90
b = ''
alf = '0123456789ABCDEF'
while a != 0:
    b += str(alf[(a%16)])
    a = a//16
b = b[::-1]
c = 0
a = max(b)
#for i in b:
    #if i == '0':
       # b = b.replace('0',a,1)
for i in b:
    if '66' in b:
        c+=1
print(b.count('66'))
