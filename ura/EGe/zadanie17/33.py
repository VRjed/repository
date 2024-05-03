g = []
for i in range(1000,10000):
    if i % 7 != 0 and i % 5 != 0 and i % 11 != 0:
        d = i
        b = ''
        while i > 0:
            b += str(i%3)
            i = i // 3
        b = b[::-1]
        if len(b) == 8:
            g.append(d)
print(max(g),min(g))