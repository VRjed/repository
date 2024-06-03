c = 0
for n in range(3,10001):
    a = '9' + n * '0'
    while '90' in a or '300' in a or '000' in a:
        if '90' in a:
            a = a.replace('90','0',1)
        if '300' in a:
            a = a.replace('300','09',1)
        if '000' in a:
            a = a.replace('000','3',1)
    if a.count('9') == 2:
        c += 1
print(c)

