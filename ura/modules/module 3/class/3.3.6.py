spi = input().split('+')
spi2 = []
for i in spi:
    b = i.find("x")
    spi2.append(i[:b])
s = ' '.join(spi2)
spi2 = list(map(int, s[:-1].split()))
print(spi2)