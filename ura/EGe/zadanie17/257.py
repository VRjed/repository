c = 0
d = []
n = []
v = 0
j = 0
max_7 = 0
min_7 = 100000
max_11 = 0
min_11 = 100000
k = 0
a = list(map(int, open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-257.txt').readlines()))
for i in a:
    if i % 7 == 0:
        c += 1
        max_7 = max(max_7,i)
        min_7 = min(min_7,i)
    if i % 11 == 0:
        k += 1
        max_11 = max(max_11,i)
        min_11 = min(min_11,i)



if min_7 > min_11:   
    print(c,max_7)
else:
    print(k,max_11)
