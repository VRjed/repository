f = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\repository\\ura\\EGe\\zadanie26\\26-s1.txt')
c = sorted(list(map(int,f.readlines())))
v = len(c)
b = c.copy()
b = sorted(b,reverse=True)
b = b[:len(b)//2]
c = c[:len(c)//2]
d = []
for i in range(len(b)):
    d.append(b[i])
    d.append(c[i])
print(d)
h = 0
q = 0
v = []
for i in range(0,len(d)):
    q += 1
    if q == v:
        break
    if i % 2 != 0:
        if d[i] > 100:
            h += d[i] * 0.9
            v.append(d[i])
            d.remove(d[i])
    
h = round(h)
print(sum(d) + h,max(v))
