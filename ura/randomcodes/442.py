h = 0
for x in range(71):
    for y in range(81):
        a = 2*71**3 + x*71**2 + x*71 + 3
        b = 4*73**3 + 8*73**2 + x*73 + 4
        c = 7*78**3 + x*78**2 + 6*78 + 5
        d = 3*81**3 + x*81**2 + y*81 + 9
        if (a+b+c-d) > 0 and (a+b+c-d) %1234 == 0:
            h += x + y
print(h)