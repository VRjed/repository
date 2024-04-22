def A(i):
    for x in range(1,3000):
        for y in range(1,3000):
            a = (y - x < i) or (7*x + 4*y > 350) or (3*y -2*x >45)
            if not a:
                return False
    return True
for i in range(1,1000):
    if (A(i)):
        print(i)
        break