def F(n,m):
    if n % m == 0:
        return True
    return False
def A(i):
    for x in range(1,1000):
        a = (F(x,3) <= (not(F(x,5)))) or ((x + i) >= 70)
        if not a:
            return False
    return True
for i in range(1,1000):
    if A(i):
        print(i)
        break
