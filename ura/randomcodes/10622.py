P = range (43,50)
Q = range (44,54)
def F(A):
    for x in range(-1000,1000):
        f = ((x in A) <= (x in P)) or (x in Q)
        if not f:
            return False
    return True
mx = -100
for left in range(20,60):
    for right in range(left + 1, 61):
        a = range(left,right +1 )
        if F(a) and mx < right - left:
            mx = right - left
            print(left, right,mx)
