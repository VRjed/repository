name = input().split()
num = list(map(int,input().split()))
d = {}
for i in range(len(num)):
    d[name[i]]=num[i]
if "Bob" in d:
    if d["Bob"] <5:
        d["Bob"] += 1
else:
    d["Bob"] = 1
b = dict(sorted(d.items()))
print(b)