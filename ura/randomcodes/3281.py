def A(i):
    for x in range(1,500):
        for y in range(1,500):
            for z in range(1,500):
                a = (220 != y + 2*x + z) or (i <6*x) or (i<y) or (i<2*z)
                if not a:
                    return False
    return True
for i in range(250,1,-1):
    if (A(i)):
        print(i)
        break
        