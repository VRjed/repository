a = open("C:\\Users\\VR1\\Desktop\\repository\\ura\\randomcodes\\asd.txt")
count = 0
for i in a.readlines():
    b = list(map(float,i.split()))
    d = {}
    x = 0
    for j in b:
        if j in d:
            d[j] += 1
        else:
            d[j] = 1
    for j in d:
        if d[j] == 2:
            x += 1
    if x == 1:
        count +=1
    for j in b:

  
        
    


   
print(count)