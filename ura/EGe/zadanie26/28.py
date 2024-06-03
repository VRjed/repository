f = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\repository\\ura\\EGe\\zadanie26\\26-J3.txt')
a,b = map(int,f.readline().split())
d = list(map(int,f.readlines()))
v = sorted(d,reverse=True)
d = []
for i in range(len(v)):
    if a - v[i] >= 0:
        a = a - v[i]
        d.append(v[i])
    if a - v[i] < 0:
        continue
print(len(d),min(d))
