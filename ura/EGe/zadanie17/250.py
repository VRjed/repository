c = 0
d = []
n = []
v = 0
j = 0
a = list(map(int, open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-243.txt').readlines()))
for i in a:
    if i % 171 == 0:
        d.append(i)
v = max(d)
for i in range(0,len(a) - 1):
    if (a[i] > v) or (a[i+1] > v) :
        if '11' in str(a[i]) or '11' in str(a[i+1]):
            c += 1
            n.append(a[i] + a[i+1])
print(c,min(n))
     
