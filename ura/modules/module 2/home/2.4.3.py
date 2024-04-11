#import math as m
#print(m.factorial(int(input())))

n = int(input())
n = n + 1
b = 1
for i in range(1,n):
    b = b * i
print(b)
