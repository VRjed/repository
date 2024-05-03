c = 0
def b(x):
    return oct(x)[2:]
d = []
n = []
f = []
v = 0
j = 0
a = list(map(int, open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-335.txt').readlines()))
for i in a:
    f.append(i)
    if i % 43 == 0:
        d.append(i)
v = min(d)
for i in range(0,len(a) - 1):
    if (a[i] + a[i+1] % v == 0) or (str(a[i])[-1] == str(v)[-1] or str(a[i+1])[-1] == str(v)[-1]):
        k = (a[i] + a[i+1]) / 2
        if k >= v:
            c += 1
            h = 0
            q = 0
            n.append(max(a[i],a[i+1]))
print(c,max(n))
