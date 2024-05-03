c = 0
def suma(x):
    h = 0
    for i in str(abs(x)):
        h += int(i)
    return h

d = []
n = []
a = list(map(int, open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-374.txt').readlines()))
for i in a:
    if abs(i) >= 100 and abs(i) <= 999 and suma(abs(i)) % 10 == 3:
        d.append(i)
v = max(d)
print(v)
for i in range(0,len(a) - 1):
    k = a[i]**2 + a[i+1]**2

    if (abs(a[i]) % 2 == 0) + (abs(a[i+1]) % 2 == 0) == 1:
        if k % v == 0:

            c += 1
            n.append(a[i]**2 + a[i+1]**2 )
print(c,max(n)