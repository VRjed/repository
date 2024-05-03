c = 0
d = []
v = 0
j = 0
a = list(map(int, open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-1.txt').readlines()))
for i in a:
    j += i
    v += 1
v = j/v
for i in range(0,len(a) - 2):
    if (a[i] < v) + (a[i+1] < v) + (a[i+2] < v) >= 2:
        if (a[i] % 19 == 0) + (a[i+1] % 19 == 0) + (a[i+2] % 19 == 0) >= 2:
            c += 1
            d.append(a[i] + a[i+1] + a[i+2])
print(c,max(d))
      
