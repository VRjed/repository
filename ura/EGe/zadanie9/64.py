a = open('C:\\Users\\VR1\Desktop\\repository\\ura\\EGe\\zadanie9\\64.txt')
count = 0
for i in a.readlines():
    b = list(map(float, i.split()))
    d = {}
    for j in b:
        if j in d:
            d[j] += 1
        else:
            d[j] = 1 
    if d

print(count)