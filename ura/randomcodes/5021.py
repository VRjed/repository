def F(n,m):
    if n % m == 0:
        return True
    return False
def A(i):
    for x in range(1,3000):
        a = (F(x,250) <= (not(F(x,10)))) or (3*x + 2*i >= 1000)
        if not a:
            return False
    return True
for i in range(1000):
    if A(i):
        print(i)
        break
