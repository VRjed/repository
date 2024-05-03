c = 0
d =[]
a = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-4.txt')
for i in a.readlines():
    if i[3] == '2' or i[3] == '7':
        if int(i) % 3 == 0 and int(i) % 11 == 0:
            c += 1
            d.append(int(i))
            
print(c,min(d))