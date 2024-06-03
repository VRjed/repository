f = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\repository\\ura\\randomcodes\\zadanie9.2.txt')
count = 0
for i in f.readlines():
    b = list(map(float, i.split()))
    d = {}
    for j in b:
        if j in d:
            d[j] += 1
        else:
            d[j] = 1

    d = sorted(d)
    
    if len(d) == 4:
        if d[-1] < d[0] + d[1] + d[2]:
            a = d[0] + d[-1]
            g = d[1] + d[2]
            c = d[0] + d[1]
            v = d[2] + d[-1]
    
            if a == g or c == v:
                count += 1

print(count)