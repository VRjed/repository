c = 0
d = []
n = []
v = 0
j = 0
mn = 1000000
a = list(map(int, open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-297.txt').readlines()))
for i in a:
    if i % 51 == 0:
        d.append(i)
v = max(d)
for i in range(0,len(a) - 1):
    if int(str(a[i+1])[-1]) == 0 or int(str(a[i])[-1]) == 0:
        continue
    if (a[i] // int(str(a[i])[-1])  == 51) + (a[i+1] // int(str(a[i+1])[-1])  == 51) == 1:
        k = (a[i] + a[i+1]) / 2
    
        
        if v > a[i] + a[i+1]:
            n.append(a[i] + a[i+1])
            c += 1

            
print(c,max(n))
