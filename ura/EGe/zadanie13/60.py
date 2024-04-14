from ipaddress import *
for i in range(32):
    n = ip_network("145.192.186.230/" + str(i),0)
    p = str(n).split("/")
    if p[0] == '145.192.160.0':
        print(n.netmask)
#255.255.224.0
#224