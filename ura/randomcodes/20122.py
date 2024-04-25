P = range(0,11)
Q = range(25,51)
def F(A):
    for x in range(-1000,1000):
        f = (x not in A) <= ((x not in P) and (x not in Q))
        if not f:
            return False
    return True
mn = 1000
for left in range(-1,60):
    for right in range(left +1 , 61):
        w = range(left,right +1 )
        if (F(w) and mn > right - left):
            mn = right - left
            print(left, right,mn)