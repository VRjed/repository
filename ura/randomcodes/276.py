a = 100**2 + 625**25 + 5**100 
b = ''
alf = '0123456789№#@$*'
while a != 0:
    b += str(alf[a%15])
    a = a //15
b = b[::-1]
h = 0
for j in b:
    if  j == "@":
        h+=1
print(h)