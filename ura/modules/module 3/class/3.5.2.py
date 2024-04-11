a = set(input().split(' '))
b = set(input().split(' '))
c = a - b
c = list(c)
c.sort()
print(' '.join(c))