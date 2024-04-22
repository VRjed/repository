for x in range(1,10010):
    a = 64**12-8**14+x
    b = ''
    while a != 0:
        b += str(a%8)
        a = a //8
    b = b[::-1]
    h = 0
    #for j in b:
        #h += int(j)
    if b.count('7') == 12 and b.count('1')==1:
        print(x)
        break