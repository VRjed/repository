def A(i):
    for x in range(1,3000):
        for y in range(1,3000):
            a = (2*y - x < i) or (x + 2*y > 50) or (2*x + y < 40)
            if not a:
                return False
    return True
for i in range(0,1000):
    if (A(i)):
        print(i)
        break