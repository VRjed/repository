def A(i):
    for x in range(5000):
        for y in range(5000):
            a = (y + 5*x < i) or (3*x + 2 * y > 81)
            if not a:
                return False
    return True
for i in range(0,1000):
    if A(i):
        print(i)
        break