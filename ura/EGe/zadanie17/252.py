c = 0
def b(x):
    return oct(x)[2:]
d = []
n = []
v = 0
j = 0
a = list(map(int, open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-243.txt').readlines()))
for i in a:
    if i % 133 == 0:
        d.append(i)
v = max(d)
for i in range(0,len(a) - 1):
    if (a[i] > v) or (a[i+1] > v) :
        if '3' in b(a[i]) or '3' in b(a[i+1]):
            c += 1
            n.append(a[i] + a[i+1])
print(c,min(n))
