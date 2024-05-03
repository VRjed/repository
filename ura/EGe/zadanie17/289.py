d = []
b = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-288.txt').readlines()
c = 0
a = []
for i in b:
    a.append(int(i))
for i in range(0,len(a) - 3):
    if (abs(a[i]) % 10 == 3) or (abs(a[i+1]) % 10 == 3) or (abs(a[i+2]) % 10 == 3) or (abs(a[i+3]) % 10 == 3):
        print(1)
        if abs(a[i]) % 7 != 3 and abs(a[i+1]) % 7 != 3 and abs(a[i+2]) % 7 != 3 and abs(a[i+3]) % 7 != 3:
            c += 1
            
            d.append(int(max(a[i],a[i+1],a[i+2],a[i+3]))- int(min(a[i],a[i+1],a[i+2],a[i+3])))
print(c,min(d))
