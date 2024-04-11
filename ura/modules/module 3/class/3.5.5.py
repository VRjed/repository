a = set(input())
b = set(input())
c = a | b
c = list(c)
c.sort()
print(c)
c = a & b
c = list(c)
c.sort()
print(c)
c = a - b
c = list(c)
c.sort()
print(c)
c = a ^ b
c = list(c)
c.sort()
print(c)