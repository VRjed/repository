def F(n,m):
    if n % m == 0:
        return True
    return False
def A(i):
    for x in range(1,3000):
        a = F(120,i) and ((not(F(x,i)) and F(x,18)) <= (not(F(x,24))))
        if not a:
            return False
    return True
for i in range(1000,0,-1):
    if A(i):
        print(i)
        break
