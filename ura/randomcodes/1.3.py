def f(n):
    b = ''
    while n != 0:
        b += str(n % 4)
        n = n // 4
    c = b[::-1]
    if n % 4 == 0:
        c = c + c[-1] + c[-2]
    else:
        g = n % 4
        h = four(g)
        c = c + h
    return int(c,4)

def four(n):
    n = n * 2
    while n != 0:
        b += str(n % 4)
        n = n // 4
    h = b[::-1]
    return h
for i in range(4,10000):
    if f(i) < 261:
        print(i)
