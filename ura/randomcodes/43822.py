P = range(11,29)
Q = range(5,56)
def f(A):
    for x in range(-1000,1000):
        f = (x in A) and (not((not(x in P)) <= (x in Q)))
        if f:
            return False
    return True
mx = -100
for l in range(0,60):
    for r in range(l + 1, 61):
        a = range(l, r + 1)
        if f(a) and mx < r - l:
            mx = r - l
            print(l, r,mx )