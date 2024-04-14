from ipaddress import *
n = ip_network('224.24.254.134/255.255.224.0',0)
for ip in n:
    print(ip)
    break
#224.24.224.0
#DFDH