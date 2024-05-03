c = 0
def b(x):
    return oct(x)[2:]
d = []
n = 0
f = []
v = 0
j = 0
mn = 1000000
a = list(map(int, open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-336.txt').readlines()))
for i in a:
    f.append(i)
    if i % 8 == 0 and i != 8:
        d.append(i)
v = min(d)
for i in range(0,len(a) - 1):
    if (a[i] % v == 0 and a[i+1] % v == 0):
        k = (a[i] + a[i+1]) / 2
    
        c += 1
        if mn > a[i] + a[i+1]:
            mn = a[i] + a[i+1]
            n = max(a[i] , a[i+1])

            
print(c,n)
