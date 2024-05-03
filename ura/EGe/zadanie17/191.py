def sistem(x,y):
    b = ''
    alf = '0123456789ABCDEF'
    while x > 0:
        b += alf[(x % y)]
        x = x // y
    b = b[::-1]
    return b
c = 0
d = []
a = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-7.txt').readlines()
for i in a:
    k = sistem(int(i),16)
    if k[-1] == "9" and k[-2] != 'A':
        c += 1
        d.append(int(i))
print(c,max(d))