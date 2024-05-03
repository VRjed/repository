c = 0
d = []
a = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-7.txt').readlines()
for i in a:
    h = 0
    i = int(i)
    for j in str(i):
        h += int(j)
    if h % 3 == 0:
        c += 1
        d.append(int(i))
print(c,max(d))