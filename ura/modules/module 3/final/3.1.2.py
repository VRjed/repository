a = int(input())
d = set()
g = 0
for g in range(a):
    c = set(input().split(' '))
    a += 1
    d = d|c
    g += 1
    if g == a:
        break
b = list(d)
b.sort()
for i in b:
    print(i)