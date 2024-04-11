def F(n):
    c = bin(n)[2:]
    if c.count('1') % 3 == 0:
        c = c + c[0] + c[1]
    else:
        c = c + bin((c.count('1') % 3)*3)[2:]
    return int(c,2)



for i in range(1,1000):
    if F(i) <= 60:
        print(i)
        


print(bin(14)[2:])
print(int('111011',2))




