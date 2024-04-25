P = range(12,29)
Q = range(15,31)
def F(a):
    for x in range(-1000,1000):
        f = ((x in P) <= (x in a)) and ((x not in Q) or (x in a))
        if not f:
            return False
    return True
mn = 1000
for left in range(1,60):
    for right in range(left +1 , 61):
        w = range(left,right +1 )
        if (F(w) and mn > right - left):
            mn = right - left
            print(left, right,mn)