def A(i):
    for x in range(1,3000):
        for y in range(1,3000):
            a = (y - x > i) or (x+4*y>40) or (y - 2*x < -35)
            if not a:
                return False
    return True
for i in range(1000,-1000,-1):
    if (A(i)):
        print(i)
        break
        
