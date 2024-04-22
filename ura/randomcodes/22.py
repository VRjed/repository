c = 0
for i in range(2,11):
    b = ''
    a = 437
    while a != 0:
        b += str((a%i))
        a = a//i
    b = b[::-1]
    h = 0
    n = 0
    for j in b:
        h += int(j)
    for j in range(2,h//2 + 1):
        if h % j == 0:
            n += 1
    if n == 0:
        c += i



a = max(b)
#for i in b:
    #if i == '0':
       # b = b.replace('0',a,1)

print(c)
