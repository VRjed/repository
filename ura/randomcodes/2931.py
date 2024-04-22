def A(i):
    for x in range(5000):
        for y in range(5000):
            a = (7*y + x < i) or (2*x + 3 * y > 98)
            if not a:
                return False
    return True
for i in range(0,1000):
    if A(i):
        print(i)
        break