P = range (5,31)
Q = range (14,24)
def F(A):
    for x in range(-1000,1000):
        f = ((x in P) == (x in Q)) <= (not(x in A))
        if not f:
            return False
    return True
mx = -100
for l in range(1,40):
    for r in range(l + 1, 41):
        a = range(l,r + 1 )
        if F(a) and mx < r - l:
            mx = r - l
            print(l ,r,mx)
# 8 + 1 = 9