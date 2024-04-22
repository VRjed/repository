def A(i):
    for x in range(5000):
        for y in range(5000):
            a = (y + 2*x < i) or (x > 20) or (y > 40)
            if not a:
                return False
    return True
for i in range(0,1000):
    if A(i):
        print(i)
        break