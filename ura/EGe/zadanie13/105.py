from ipaddress import *
for i in range(32):
    n = ip_network('125.181.67.15/'+str(i),0)
    p=str(n).split('/')
    if p[0] == '125.181.64.0':
        a = bin(int(n.netmask))[2:].zfill(32)
        c = 0
        for j in a:
            if j == '0':
                c += 1
        print(c)
#14