a = 2*27**7 + 3**10 - 9
b = ''
while a != 0:
    b += str(a%3)
    a = a //3
b = b[::-1]
b = b.count('0')
print(b)