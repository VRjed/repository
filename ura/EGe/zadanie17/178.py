a = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-4.txt')
d = 0
b = []
for i in a.readlines():
    c = 0
    if int(i) % 2 == 0:
        c += 1
    if int(i) % 3 == 0:
        c += 1
    if int(i) % 5 == 0:
        c += 1
    if int(i) % 7 == 0:
        c += 1
    if c == 2:
        d += 1
        b.append(i)
g = int(min(b))
j = int(max(b))

print(d)
print(g + j)