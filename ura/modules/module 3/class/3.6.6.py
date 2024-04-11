name = input().split()

d = {}
for i in range(len(name)):
    d[name[i]]=len(name[i])
b = dict(sorted(d.items()))
print(b)