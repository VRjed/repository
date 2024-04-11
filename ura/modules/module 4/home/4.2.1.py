def exchange(n, v):
    c = list(n)
    n[:] = list(v)
    v[:] = c
    print(n,v)