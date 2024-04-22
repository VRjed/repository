a = 4*125**4 - 25**4 + 9  
b = ''
while a != 0:
    b += str(a%5)
    a = a //5
b = b[::-1]
b = b.count('4')
print(b)