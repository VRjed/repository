P = range(7,16)
Q = range(12,26)
def F(A):
    for x in range(-1000,1000):
        f = ((x not in P) or (x in A)) and ((x not in Q) or (x in A))
        if not f:
            return False
    return True
mn = 1000
for left in range(-1,60):
    for right in range(left +1 , 61):
        w = range(left,right +1 )
        if (F(w) and mn > right - left):
            mn = right - left
            print(left, right,mn, mn/2)