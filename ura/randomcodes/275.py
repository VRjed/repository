a = 32**2 + 1024 + 1024**2 
b = ''
alf = '0123456789ABCDEF'
while a != 0:
    b += str(alf[a%16])
    a = a //16
b = b[::-1]
h = 0
for j in b:
    if  j == "0":
        h+=1
print(h)