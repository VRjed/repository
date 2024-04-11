def f(n):
    c = str(n)
    c3 = int(c[0]) + int(c[1])
    c4 = int(c[2]) + int(c[3])
    if c3 > c4:
        c = str(c3) + str(c4)
    else:
        c = str(c4) + str(c3)
    return c

for i in range(1000, 10000):
    if f(i) == '1412':
        print(i)
        break