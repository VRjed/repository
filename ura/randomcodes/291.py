for x in range(1,10010):
    a = 125**7 - 25**4 + x 
    b = ''
    while a != 0:
        b += str(a%5)
        a = a //5
    b = b[::-1]
    h = 0
    #for j in b:
        #h += int(j)
    if b.count('4') == 15 and b.count('1')==2 and b.count('3')==1:
        print(x)
        break