from ipaddress import *
for i in range(32):
    n = ip_network('134.92.108.145/'+ str(i),0)
    part = str(n).split('/')
    if part[0] == '134.92.104.0':
        print(n.netmask)
#255.255.248.0
#248