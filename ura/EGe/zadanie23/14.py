def f(x,y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x+3,y) + f(x*3 ,y)
print(f(5,27))