for x in range(1,10010):
    a = 27**7 - 3**11 + 36 - x 
    b = ''
    while a != 0:
        b += str(a%3)
        a = a //3
    b = b[::-1]
    h = 0
    for j in b:
        h += int(j)
    if h==22:
        print(x)
        break