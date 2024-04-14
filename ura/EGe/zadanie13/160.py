from ipaddress import *
c =0
n = ip_network('211.48.136.64/255.255.255.224',0)
for ip in n:
    a = bin(int(ip))[2:]
    if a[-1] == '1' and a[-2] == '1':
        c +=1
print(c)
#8