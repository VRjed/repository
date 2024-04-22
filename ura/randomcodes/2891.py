def A(i):
    for x in range(5000):
        for y in range(5000):
            a = (2*y + 5*x < i) or (x+y>80)
            if not a:
                return False
    return True
for i in range(0,1000):
    if (A(i)):
        print(i)
        break
