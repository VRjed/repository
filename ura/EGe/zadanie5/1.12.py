def f(n):
    c = bin(n)[2:]
    if c[-1] == '0':
        c = c[:-1] + c[0] + c[1]
    else:
        return None
    s = c[::-1]
    return int(s,2)
for i in range(1, 1000):
    if f(i) == 119:
        print(i)
