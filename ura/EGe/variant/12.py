a = '3' + 75 * '6'
while '3' in a:
    if '36' in a:
        a = a.replace('36','6',1)
    else:
        a = a.replace('3','6',1)
print(a.count('6'))