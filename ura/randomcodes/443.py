h = 1
for x in range(12):
    for y in range(18):
        a = 6*12**4 + 7*12**3 + x*12**2 + x*12 + 3
        b = 2*14**3 + x*14**2 + 9*14 + x
        c = 4*15**4 + 4*15**3 + x*15**2 + x*15 + 3 
        d = 2*18**3 + x*18**2 + y*18 + 7
        if (a+b+c-d) > 0 and (a+b+c-d) %77 == 0:
            h *= x * y
print(h)