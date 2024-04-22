def A(i):
    for x in range(1,2000):
        for y in range(1,2000):
            a = (4*y - x > i) or (x + 6*y < 210) or (3*y - 2*x <30)
            if not a:
                return False
    return True
for i in range(1000,-1000,-1):
    if (A(i)):
        print(i)
        break