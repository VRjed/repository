from ipaddress import *
c = 0
for i in range(32):
    n = ip_network('18.168.250.32/'+str(i),0)
    p = str(n).split('/')
    if p[0]=='18.168.240.0':
        c += 1
print(c)
#1