def F(n,m):
    if n % m == 0:
        return True
    return False
def A(i):
    for x in range(3000):
        a = F(110,i) and ((F(x,80) and F(x,75)) <= F(x,i))
        if not a:
            return False
    return True
for i in range(1000,1,-1):
    if A(i):
        print(i)
        break
