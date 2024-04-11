a = set(map(int,input().split(' ')))
b = set(map(int,input().split(' ')))
c = a & b
c = list(c)
c.sort()
if len(c) > 0:
    print(*c)
else:
    print('set()')