c = 0
from fnmatch import *
def pro(x):
    res = 1
    for d in str(x):
        if int(d) % 2 == 0:
            res *= int(d)
    return res
d = []
n = []
f = []
v = 0
j = 0
mn = 1000000
a = list(map(int, open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-346.txt').readlines()))
for i in a:
    f.append(i)
    if i % 8 == 0 and i != 8:
        d.append(i)
v = min(d)
for i in range(0,len(a) - 2):
    k = pro(a[i]) * pro(a[i+1]) * pro(a[i+2])
    if k <= 2 * 10 ** 9 and fnmatch(str(k),"25*2*"):
        c += 1
        n.append(k)
            
print(c,max(n))