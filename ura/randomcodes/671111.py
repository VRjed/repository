import sys
sys.setrecursionlimit(1000000)
c = 0
def f(n):
    if n < 3:
        return n + 1
    if n >= 3 and n % 2 == 0:
        return n + 2 * f(n + 2)
    if n >= 3 and n % 2 != 0:
        return f(n-2)+ n-2
for i in range(1,10000,2):
    if 100 <= f(i) <= 999:
        
            c += 1
print(c)