def F(n,m):
    if n % m == 0:
        return True
    return False
def A(i):
    for x in range(1,1000):
        a = (F(x,175) <= (not(F(x,25)))) or (2*x + i >= 1780)
        if not a:
            return False
    return True
for i in range(10000):
    if A(i):
        print(i)
        break
