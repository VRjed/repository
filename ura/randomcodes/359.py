for y in range(11):
    for x in range(11):
        a = int('7' + str(y) + '23' + str(x) + '5',25)
        b = int('67' + str(x) + '9'+str(y),11)
        if (a+b)%131 == 0:
            print((a+b)/131)