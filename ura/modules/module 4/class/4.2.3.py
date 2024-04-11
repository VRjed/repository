def min_max(n, type='min'):
    count = 0
    if type == 'min':
        c = min(n)
    else:
        c = max(n)
    for i in n:
        if i == c:
            count += 1
    return count
