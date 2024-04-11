def count_without_8(n):
    n = list(map(str,n))
    c = 0
    for i in n:
        if i.count('8') == 0:
            c += 1
    return c
