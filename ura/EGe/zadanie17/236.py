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
    j =0
    if a[i] > v:
        j += 1
    if a[i+1] > v:
        j += 1
    if a[i+2] > v:
        j += 1
    if j >= 2:
        if a[i] % 11 == 0 or a[i+1] % 11 == 0 or a[i+2] % 11 == 0:
            c += 1
            d.append(a[i] + a[i+1] + a[i+2])
print(c,max(d))
      
