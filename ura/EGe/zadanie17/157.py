a = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-2.txt')
d = []
for i in a.readlines():
    d.append(int(i))
g = min(d)
c = d.count(g)
print(c)
v = 0
o = 0
for i in d:
    v += 1
    if i == g:
        o += 1
        if o == 3:
            break

print(c,v)