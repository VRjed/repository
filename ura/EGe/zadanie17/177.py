a = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-4.txt')
c = 0
d = []
for i in a.readlines():
    if str(i).count('0') >=2:
        if int(i) % 7 == 0:
            c += 1
            d.append(i)
print(max(d),c)