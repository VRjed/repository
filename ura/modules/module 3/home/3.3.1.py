a = input().split(' ')
f = []
for i in a:
    i = int(i)
    f.insert(i + 1, i)
p = len(f) // 2
b = f[:p]
b.reverse()
v = f[p:]
v.reverse()
print(b+v)