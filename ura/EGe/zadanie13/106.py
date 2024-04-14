from ipaddress import *
for i in range(32):
    n = ip_network('212.168.104.5/'+str(i),0)
    p = str(n).split('/')
    if p[0]=='212.168.104.0':
        a = bin(int(n.netmask))[2:].zfill(32)
        c = 0
        for j in a:
            if j == "0":
                c += 1
        print(c)
#3