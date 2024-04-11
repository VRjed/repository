n = int(input())
c6 = n // 100000
c5 = n // 10000 % 10 
c4 = n // 1000 % 10 
c3 = n // 100 % 10 
c2 = n // 10 % 10
c1 = n % 10
print (c1, c2 ,c3,c4,c5,c6)
c1 = str(c1)
c2 = str(c2)
c3 = str(c3)
c4 = str(c4)
c5 = str(c5)
c6 = str(c6)

print(c1 ,c2, c3, c4,c5,c6,sep = '')
c6 = n // 100000
c5 = n // 10000 % 10 
c4 = n // 1000 % 10 
c3 = n // 100 % 10 
c2 = n // 10 % 10
c1 = n % 10
n1 = c1 * 100000 + c2 * 10000 + c3*1000 +c4*100+c5*10+c6
g = n/n1
print(n , ' / ' , n1, ' = ' , format(g,'1.6f'),sep = '')