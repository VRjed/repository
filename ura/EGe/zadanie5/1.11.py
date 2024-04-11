def f(n):
    c = bin(n)[2:]
    count1 = 0
    count0 = 0
    b = 0
    for i in c:
        if i == '1':
            count1 += 1
        else:
            count0 += 1
    for i in c:
        b += int(i)
    c = c + str(b%2)
    if count1 > count0:
        c = c + '0'
    else:
        c = c + '1'
    return int(c, 2)
count12 = 0
for i in range(1 , 10000):
    if f(i) >= 50 and f(i) <= 80:
        count12 += 1
print(count12)