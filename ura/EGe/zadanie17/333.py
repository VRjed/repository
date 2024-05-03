c = 0
def b(x):
    return oct(x)[2:]
d = []
n = []
f = []
v = 0
j = 0
a = list(map(int, open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-333.txt').readlines()))
for i in a:
    f.append(i)
    if i >= 1000:
        d.append(i)
v = sum(d)/len(d)
for i in range(0,len(a) - 1):
    k = a[i] + a[i+1]
    if k not in f:
        if k < v:
            c += 1
            h = 0
            q = 0
            for j in str(a[i]):
                h += int(j)
            for j in str(a[i+1]):
                q += int(j)
            n.append(h+q)
print(c,max(n))
