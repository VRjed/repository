c = 0
d = []
v = 0
j = 0
a = list(map(int, open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-1.txt').readlines()))
for i in a:
    j += i
    v += 1
v = j/v
for i in range(0,len(a) - 1):
    if a[i] > v and a[i+1] > v:
        k = a[i] + a[i+1]
        if str(k)[-2] == '3' and str(k)[-1] == '1':
            c += 1
            d.append(a[i] + a[i+1])
print(c,max(d))
      
