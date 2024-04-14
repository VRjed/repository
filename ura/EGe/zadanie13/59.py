from ipaddress import *
for i in range(32):
    n = ip_network('145.192.94.230/'+ str(i),0)
    p = str(n).split('/')
    if p[0] == '145.192.80.0':
        print(n.netmask)
#255.255.240.0
#240
