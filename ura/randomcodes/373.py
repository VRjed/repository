for i in range(10):
    a = 1 * int('123' + str(i) + '4')**2 + 1 * int('123' + str(i) + '4') + 3
    b = 1 * int('124' + str(i)+'3')**2 + 2 * int('124' + str(i)+'3') + 2
    if (a + b) % 10 == 0:
        print((a+b)//10)