from ipaddress import *
n = ip_network('204.230.250.29/255.255.240.0',0)
for ip in n:
    print(ip)
    break
#204.230.240.0
#DEFA