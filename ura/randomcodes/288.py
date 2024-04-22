for x in range(1,1001):
    a = 36**17-6**x+71
    b = ''
    while a != 0:
        b += str(a%6)
        a = a //6
    b = b[::-1]
    h = 0
    for j in b:
        h += int(j)
    if h == 61:
        print(x)