def f(n):
    c = bin(n)[2:]
    if c.count('1') % 2 == 0:
        c = c + '0'
    else:
        c = c + '1'
    c = c + '0'
    return int(c, 2)
for i in range(1, 10000):
    if f(i) > 103:
        print(i)
        break