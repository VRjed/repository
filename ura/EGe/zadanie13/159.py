from ipaddress import *
c =0
n = ip_network('158.132.161.128/255.255.255.128',0)
for ip in n:
    a = bin(int(ip))[2:]
    if a[-1] == '1':
        c +=1
print(c)
#64