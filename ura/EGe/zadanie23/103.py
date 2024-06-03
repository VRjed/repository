def f(x,y,z):
    if x > y or z > 6:
        return 0
    if x == y and z == 6:
        return 1
    return f(x + 1,y,z+ 1) + f(x + 2,y,z +1) + f(x * 2,y,z +1) 
print(f(1,20,0))