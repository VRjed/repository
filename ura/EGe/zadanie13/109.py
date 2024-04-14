from ipaddress import *
c = 0
for i in range(32):
    n = ip_network('208.207.230.65/'+str(i),0)
    p = str(n).split('/')
    if p[0]=='208.207.224.0':
        c += 1
print(c)
#3