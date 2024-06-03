f = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\repository\\ura\\EGe\\zadanie24\\k7-70.txt').readline()
c = 0
max = 0
l = ''
max_l = ''
for i in f:
    if i in 'C':
        c += 1
        l += i
        if c > max:
            max = c
            max_l = l
    else:
        c = 0
        l = ''

print(max,max_l)
i = f[0]
while 'C'*(c+1) in f:
    c += 1
print(c)

print(len('CCCCCCCCCCCCCCCCCCCCCCCCCCCCCC'))