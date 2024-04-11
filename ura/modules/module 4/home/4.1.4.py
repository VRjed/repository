def length(x):
    if x < 0:
        c = len(str(x)[1:])
    else:
        c = len(str(x))
    return c