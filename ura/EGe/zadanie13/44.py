from ipaddress import *
n = ip_network('217.19.128.131/255.255.192.0',0)
for ip in n:
    print(ip)
    break
#217.19.128.0
#HCEA