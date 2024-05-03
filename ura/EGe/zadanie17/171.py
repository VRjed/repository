a = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-4.txt')
c = 0
d = []
def sistem(x,y):
    b = ''
    while x > 0:
        b += str(x % y)
        x = x // y
    b = b[::-1]
    return b
for i in a.readlines():
    if sistem(int(i),3)[-1] == sistem(int(i),5)[-1] :
        if int(i) % 31 == 0 or int(i) % 47 == 0 or int(i) % 53 == 0 :
            c += 1
            d.append(int(i))
print(c,min(d))
