def A(i):
    for x in range(1,3000):
        for y in range(1,3000):
            a = (3*y + x < i) or (3*x + 2*y > 80) or (3*x - 4*y > 90)
            if not a:
                return False
    return True
for i in range(0,1000):
    if (A(i)):
        print(i)
        break