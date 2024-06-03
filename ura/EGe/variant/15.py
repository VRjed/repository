
B = range(10,124)
C = range(45,401)
def F(A):
    for x in range(-1000,1000):
        f = (not(x in C)) <= ((x in C) or (x in A) or (not(x in B)))
        if not f:
            return False
    return True
mn = 1000
for left in range(1,420):
    for right in range(left +1 , 421):
        w = range(left,right +1 )
        if (F(w) and mn > right - left):
            mn = right - left
            print(left, right,mn)
