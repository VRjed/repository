from ipaddress import *
c =0
n = ip_network('192.168.248.176/255.255.255.240',0)
for ip in n:
    a = bin(int(ip))[2:].count('1')
    if 32 - a < 16:
        c +=1
print(c)
#1