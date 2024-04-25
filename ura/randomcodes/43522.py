P = range(12,47)
Q = range(20,31)
def f(A):
    for x in range(-1000,1000):
        f = (x in A) and not((x in P) or (x in Q))
        if f:
            return False
    return True
mx = -100
for left in range(1,55):
    for right in range(left + 1, 56):
        a = range(left , right +1)
        if (f(a) and mx < right - left):
            mx = right - left
            print(left , right, right - left)



































P = range (12, 27)
Q = range (30, 36)


def f(A):
    for x in range (-1000, 1000):
        f = (x in A) and not ((x in P) or (x in Q))
        if f:
            return False
    return True


mx = float("-inf")

for left in range (1, 50):
    for right in range (left + 1, 51):
        a = range (left, right + 1)
        if (f(a) and mx < right - left):
            mx = right - left
            print (left, right, right - left)