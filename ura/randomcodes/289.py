for x in range(1,1001):
    a = 81**20-9**x+50
    b = ''
    while a != 0:
        b += str(a%9)
        a = a //9
    b = b[::-1]
    h = 0
    for j in b:
        h += int(j)
    if h == 138:
        print(x)
        break