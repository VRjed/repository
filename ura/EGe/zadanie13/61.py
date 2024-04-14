from ipaddress import *
for i in range(32):
    n = ip_network('158.198.104.220/'+str(i),0)
    p = str(n).split("/")
    if p[0] == '158.198.64.0':
        print(n.netmask)
#255.255.192.0
#192