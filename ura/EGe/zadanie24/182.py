f = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\repository\\ura\\EGe\\zadanie24\\24-181.txt').readline()
c = 0
h = ''
mh = ""
#for i in f:
   # if i == '.':
    #    c += 1
#    if c <= 2:
 #       h += i
 #       if mh < h:
  #          mh = h
 #   else:
 #       h = ''
 #       c = 0
    
print(len(mh))

j = ''
n = f
for i in range(len(f)):
    v = n.find('.')
    
    h = f[:v]
    n = f[v+1:]
    if len(h) > len(j):
        j += h
print(j)
    