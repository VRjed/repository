from ipaddress import *
c = 0
for i in range(32):
    n = ip_network('218.217.212.15/'+str(i),0)
    p = str(n).split('/')
    if p[0]=='218.217.192.0':
        c += 1
print(c)
#2