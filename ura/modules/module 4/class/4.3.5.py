def my_sum(*a):
    d = [0]
    j = 0
    for i in a:
        j += i
        d.append(j)
    return d
        