P = range(10,43)
Q = range(20,37)
def f(A):
    for x in range(-1000,1000):
        f = (x in P) <= (not(x in Q) or (x in A))
        if not(f):
            return False
    return True
mn = 1000
for l in range(1,51):
    for r in range(l + 1, 52):
        a = range(l, r + 1)
        if f(a) and mn > r - l:
            mn = r - l
            print(l, r,mn )
