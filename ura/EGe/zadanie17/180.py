def sistem(x,y):
    b = ''
    while x > 0:
        b += str(x % y)
        x = x // y
    b = b[::-1]
    return b



c = 0
d =[]
a = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-4.txt')
for i in a.readlines():
    if sistem(int(i),5)[-1] == '3':
        if sistem(int(i),9)[-1] == '5':
            if sistem(int(i),8)[-1] != '7':
                c += 1
                d.append(i)
print(c,max(d))