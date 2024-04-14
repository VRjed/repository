from ipaddress import *
c =0
n = ip_network('202.75.38.176/255.255.255.240',0)
for ip in n:
    a = bin(int(ip))[2:]
    if '000' not in a or '111' not in a:
        c +=1

print(c