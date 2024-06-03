f = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\repository\\ura\\EGe\\zadanie24\\k8-52.txt').readline()
h =  f[0]
max_h = ''
for i in range(1,len(f)):
    if h[-1] == f[i]:
        h += f[i]
        if len(max_h) < len(h):
            max_h = h
    else:
        h = f[i]
print(max_h,len(max_h))