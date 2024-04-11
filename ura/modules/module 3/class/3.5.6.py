a = set(input())
b = 'AIOEU'
for i in b:
    a.discard(i)
a = list(a)
a.sort()
print(a)