f = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\repository\\ura\\EGe\\zadanie24\\k8-2.txt').readline()
h = f[0]
c = 0
max_c = 0
v = ''
max_h = ''
for i in range(1,len(f)):
    if f[i] != h[-1]:
        c += 1
        h += str(f[i])
        if len(max_h) < len(h):
            max_h = h
    else:
        h = f[i]
        c = 0
print(max_h, len(max_h))