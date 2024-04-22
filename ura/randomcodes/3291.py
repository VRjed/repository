def A(i):
    for x in range(1,500):
        for y in range(1,500):
            for z in range(1,500):
                a = (x + 3*y + 2*z - 54 != 0) or (i <x + 10) or (i<5*y - 4 * x) or (i<z + x)
                if not a:
                    return False
    return True
for i in range(250,1,-1):
    if (A(i)):
        print(i)
        break
        