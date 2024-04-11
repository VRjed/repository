n = int(input())
if n % 2 != 0:
    n = n
else:
    n = n + 1
a = [i * i for i in range(1, n) if i % 2 == 0]
print(a)