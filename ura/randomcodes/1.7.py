def f(n):
    w = n
    b = ""
    alf = '0123456789AB'
    while n != 0:
        b += alf[n % 12]
        n = n // 12
    c = b[::-1]
    
    h = 0
    b = 0
    for i in c:
        if int(i,12) > b:
            b = int(i,12)
            h = i
        
    if w % 4 == 0:
        c = '2' + c + '64'
    else:
        c = c + h
    return int(c,12)
mn = 10000000000000000000000
for i in range(1,10000):

    if f(i) > 1799:
        mn = min(mn,f(i))
        
print(mn)