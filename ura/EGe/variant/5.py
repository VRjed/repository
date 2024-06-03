def f(n):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = b + '0'
        b = '111' + b[3:]
    else:
        b = b + '1'
        b = '10' + b[2:]
    return int(b,2)
for i in range(6,1000):
    if f(i) > 58:
        print(i)
        break
print('111'[2:])
print(bin(18)[2:])
print(int('111100',2))