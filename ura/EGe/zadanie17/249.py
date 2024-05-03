c = 0
d = []
n = []
v = 0
j = 0
a = list(map(int, open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-243.txt').readlines()))
for i in a:
    if i % 211 == 0:
        d.append(i)
v = max(d)
for i in range(0,len(a) - 1):
    if (a[i] > v) or (a[i+1] > v) :
        if str(a[i]).count('1') >= 1 or str(a[i+1]).count('1') >= 1:
            c += 1
            n.append(a[i] + a[i+1])
print(c,min(n))
     
