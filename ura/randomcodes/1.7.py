def de(n,m):
    if n % m == 0:
        return True
    return False
def A(n):
    for x in range(1,3000):
        b = (not(de(x,n))) <= (de(x, 14)) <= (not(de(x,4)))
        return b
for i in range(10000,1,-1):
    if A(i):
        print(i)
        break