a = 2*9**10 - 3**5 + 5 
b = ''
while a != 0:
    b += str(a%3)
    a = a //3
b = b[::-1]
b = b.count('2')
print(b)