n = int(input())
c1 = n // 100 
c2 = n // 10 % 10 
c3 = n % 10 
n1 = c3 * 100 + c2 * 10 + c1*1
print( n * n1)
