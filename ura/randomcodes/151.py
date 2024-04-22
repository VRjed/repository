a = 5*36**7 + 6**10 - 36  
b = ''
while a != 0:
    b += str(a%6)
    a = a //6
b = b[::-1]
b = b.count('5')
print(b)