spi =  input().split()
b = int(input())
spi2 = []
for i in spi:
    i = int(i)
    spi2.append(i ** b)
print(spi2)