from ipaddress import *
for i in range(32):
    n = ip_network('221.117.97.115/'+str(i),0)
    p = str(n).split('/')
    if p[0]=='221.117.96.0':
        a = bin(int(n.netmask))[2:].zfill(32)
        c = 0
        for j in a:
            if j == "0":
                c += 1
        print(c)
#9