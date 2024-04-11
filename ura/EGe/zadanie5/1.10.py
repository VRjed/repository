def f(n):
    c = bin(n)[2:]
    if c.count('1') % 2 ==0:
        c = c + '11'
    if c.count('1') % 2 != 0 and c.count('1') % 2 == 1:
        c = c + '00'
    return int(c,2)
for i in range(1, 10000):
    if f(i) > 54:
        print(f(i))
        break
    
