P = range (15,40)
Q = range (44,58)
def F(A):
    for x in range(-1000,1000):
        f = ((x in A) <= (x in P)) or (x in Q)
        if not f:
            return False
    return True
mx = -100
for l in range(10,65):
    for r in range(l + 1, 66):
        a = range(l,r +1 )
        if F(a) and mx < r - l:
            mx = r - l
            print(l ,r,mx)
