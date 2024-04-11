def series(n):
    c = 0
    for i in range(1,n + 1):
        c += i * (i-1)
    return c