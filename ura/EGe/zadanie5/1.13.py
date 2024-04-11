def f(n):
    c = bin(n)[2:]
    b = c.count('1')
    
    if n % 2 == 0:
        c = c + bin(b)[2:]
    else:
        c = '1' + c + '00'
    return int(c,2)
count = 0
for i in range(1,10000):
    if f(i) >= 500 and f(i) <= 700:
        count += 1
print(count)
