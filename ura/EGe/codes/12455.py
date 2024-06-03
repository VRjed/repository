a = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\repository\\ura\\EGe\\codes\\12455.txt')
ct = 0
for i in a.readlines():
    b = list(map(int, i.split()))
    b.sort()
    if b[0]**2 + b[1]**2 == b[2]**2:
        ct += 1
        continue
    
    
    if str(b[1])[-1] > '7' and str(b[2])[-1] > '7' and str(b[0])[-1] > '7':
        ct += 1
print(ct)
