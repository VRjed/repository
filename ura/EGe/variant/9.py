a = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\repository\\ura\\EGe\\variant\\9.txt').readlines()
b = []
c = 0
for i in a:
   b.append(list(map(int,i.split())))
for i in b:
    b.sort()
    if i[3] < i[0] + i[1] + i[2]:
        if i[0] + i[1] != i[2] + i[3] and i[0] + i[2] != i[1] + i[3] and i[0] + i[3] != i[2] + i[1] and i[2] + i[1] != i[0] + i[3] and i[2] + i[3] != i[0] + i[1] and i[2] + i[0] != i[1] + i[3] and i[3] + i[0] != i[1] + i[2] and i[3] + i[1] != i[2] + i[0] and i[3] + i[2] != i[1] + i[0]: 
            c += 1
print(c)
                
            