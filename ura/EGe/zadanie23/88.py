def f(x,y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x+1,y) + f(x+3,y) + f(x*2,y)
print(f(1,4)*f(4,9)*f(9,13))