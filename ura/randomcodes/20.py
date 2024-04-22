a = 9**81+27**729-4
b = ''
alf = '0123456789ABCD'
while a != 0:
    b += str((a%9))
    a = a//9
b = b[::-1]
c = 0
a = max(b)
for i in b:
    if i == '0':
        b = b.replace('0',a,1)
for i in b:
    if i == a:
        c+=1
print(c)
