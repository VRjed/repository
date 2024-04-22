def A(i):
    for x in range(1,2000):
        for y in range(1,2000):
            a = (3*y - x > i) or (2*x + 3*y < 30) or (2*y - x <-31)
            if not a:
                return False
    return True
for i in range(1000,-1000,-1):
    if (A(i)):
        print(i)
        break