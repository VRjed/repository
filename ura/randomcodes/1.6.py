a = open("C:\\Users\\VR1\\Desktop\\repository\\ura\\randomcodes\\asd.txt")
count = 0
for i in a.readlines():
    b = sorted(list(map(int,i.split())))
    
    d = {}
    for j in b:
        if j in d:
            d[j] += 1
        else:
            d[j] = 1 
    k = 0
    j = b[0]
    l = b[-1]

    if len(d) <= 3:
        if (b[0] + b[-1])** 2 > sum(b[1:-1])**2:
            count += 1
    
print(count)
    

            
        
