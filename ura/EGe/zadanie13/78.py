from ipaddress import *
for i in range(31,-1,-1):
    n1 = ip_network('61.58.73.42/'+str(i),0)
    n2 = ip_network('61.58.75.136/'+str(i),0)
    p1=str(n1).split('/')
    p2=str(n2).split('/')
    if p1[0]==p2[0]:
        print(n1.netmask)
        break
#255.255.252.0
#252