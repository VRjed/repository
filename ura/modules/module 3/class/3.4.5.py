n = int(input())
a = [i * i for i in range(1, n) if i * i % 7 == 0 and i % 2 == 0]
print(a)