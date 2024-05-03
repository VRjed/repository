c = 0
def suma(x):
    h = 0
    for i in str(abs(x)):
        h += int(i)
    return h

d = []
n = []
a = list(map(int, open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-370.txt').readlines()))
for i in a:
    if 100 <= abs(i)<= 999 and suma(i) % 10 == 3:
        d.append(i)
v = max(d)
for i in range(len(a) - 1):

    if (1000<=abs(a[i])<=9999) + (1000<=abs(a[i+1])<=9999) == 1 :
        if (a[i]**2 + a[i+1]**2) % v == 0:
            c += 1
            n.append(a[i]**2 + a[i+1]**2 )
print(c,max(n))