c = 0
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
mn = 1000000
a = list(map(int, open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-390.txt').readlines()))
for i in a:
    f.append(i)
    if 100 <= abs(i):
        if str(abs(i))[-3] == '6' and str(abs(i))[-2] == '1' and str(abs(i))[-1] == '5':
            d.append(abs(i))
v = sum(d)/len(d)
for i in range(0,len(a) - 2):
    if (1000 <= (abs(a[i]) <= 9999)+ (1000 <= abs(a[i+1]) <= 9999) + (1000 <= abs(a[i+2]) <= 9999)) < 3:
        j = 0
        q = 0
        if a[i] % 5 == 0:
            j += 1
        if a[i+1] % 5 == 0:
            j += 1
        if a[i+2] % 5 == 0:
            j += 1
        if a[i] % 7 == 0:
            q += 1
        if a[i+1] % 7 == 0:
            q += 1
        if a[i+2] % 7 == 0:
            q += 1
        if j > q:
            if a[i] > v and a[i+1] > v and a[i+2] > v:
                c += 1
                n.append(a[i] + a[i+1] + a[i+32])
            
print(c,min(n))