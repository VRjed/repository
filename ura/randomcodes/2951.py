def A(i):
    for x in range(1,5000):
        for y in range(1,5000):
            a = (y + 4*x < i) or (x+4*y>120) or (5*x - 2*y >50)
            if not a:
                return False
    return True
for i in range(0,1000):
    if (A(i)):
        print(i)
        break
