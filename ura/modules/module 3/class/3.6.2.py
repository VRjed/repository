name = input().split()
num = list(map(int,input().split()))
d = {}
for i in range(len(num)):
    d[name[i]]=num[i]
d["Bob"] = 5
b = dict(sorted(d.items()))
print(b)