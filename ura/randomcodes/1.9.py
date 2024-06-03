a = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\repository\\ura\\randomcodes\\varik13.txt').readlines()
d = []
k = list(map(int,a))
for i in k:
    if i % 19 == 0:
          d.append(i)
v = min(d)
q = []
c = 0
for i in range(0, len(k) - 1):
    if k[i] % v == 0 or k[i+1] % v == 0:
        c += 1
        q.append(sum([k[i],k[i+1]]))
print(c,max(q))
