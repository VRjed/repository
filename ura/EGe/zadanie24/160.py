f = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\repository\\ura\\EGe\\zadanie24\\24-s1.txt').readlines()
mna = 1000000
k = ''
mnt = ''
for i in f:
    if i.count('A') < mna:
        for j in i:
            if i == 'A':
                k += i
        mna = len(k)
        mnt += k
        k = ''
d = {}    
for n in mnt:
    if n in d:
        d[n] += 1
    else:
        d[n] = 1
v = max(d)
print(v , d[v])
for i in f:
    pass