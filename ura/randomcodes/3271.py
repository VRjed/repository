def A(i):
    for x in range(1,100):
        for y in range(1,100):
            for z in range(1,100):
                a = (48 != y + 2*x + z) or (i < x) or (i<y) or (i<z)
                if not a:
                    return False
    return True
for i in range(100,1,-1):
    if (A(i)):
        print(i)
        break
        