a = int(input())
b = int(input())
c = int(input())
v = a
n = b
g = c
if v % 2 == 0:
    v = a // 2
else:
    v = a // 2 + 1
if n % 2 == 0:
    n = b // 2
else:
    n = b // 2 + 1
if g % 2 == 0:
    g = c // 2
else:
    g = c // 2 + 1
k = v + n + g
print (k)