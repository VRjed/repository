a = 26**2 + 169 - 11
b = ''
alf = '0123456789ABC'
while a != 0:
    b += str(alf[a%13])
    a = a //13
b = b[::-1]
h = 0
for j in b:
    if j == 'C' or j == "2":
        h+=1
print(h)