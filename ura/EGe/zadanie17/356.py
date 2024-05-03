c = 0
d = []
n = []
a = list(map(int, open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-354.txt').readlines()))
for i in a:
    if abs(i) % 10 == 1:
        d.append(i)
v = min(d)
for i in range(0,len(a) - 1):
    k = min(a[i],a[i+1])
    if abs(k) % 10 == 4:
        if a[i]**2 + a[i+1]**2 < v**2:
            c += 1
            n.append(a[i]**2 + a[i+1]**2 )
print(c,max(n))