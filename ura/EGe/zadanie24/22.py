f = 'C:\\Users\\VR1\\Desktop\\repository\\repository\\repository\\ura\\EGe\\zadanie24\\k7a-2.txt'
a = open(f).readline()
a = a.replace('A', 'C')
a = a.replace('D', 'C')
h = ''
max_h = ''
for i in a:
    if i in 'C':
        h += i
        if len(max_h) < len(h):
            max_h = h
    else:
        h = ''
print(max_h,len(max_h))
