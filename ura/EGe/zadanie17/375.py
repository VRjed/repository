c = 0
def suma(x):
    h = 0
    for i in str(abs(x)):
        h += int(i)
    return h

d = []
n = []
a = list(map(int, open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-375.txt').readlines()))
for i in a:
    if 100 <= abs(i)<= 999:
        if str(i)[0] != str(i)[-1] and str(i)[1] != str(i)[-1]:
            d.append(i)
v = min(d)
for i in range(len(a)//2):

    if ((a[i])) * (a[-i - 1]) % v == 0:
        
        c += 1
        n.append(a[i] + a[-i - 1] )
print(c,min(n))