def F(n,m):
    if n % m == 0:
        return True
    return False
def A(i):
    for x in range(1,3000):
        a = (F(x,12) <= (not(F(x,90)))) or (x + 2*i >= 512)
        if not a:
            return False
    return True
for i in range(1000):
    if A(i):
        print(i)
        break
