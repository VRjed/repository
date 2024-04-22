for i in range(10):
    a = 1 * int('123' + str(i) + '4')**2 + 1
    b = 1 * int('1' + str(i)+'243')**2 + 2* int('1' + str(i) + '243') + 3
    if (a + b) % 25 == 0:
        print((a+b)//25)
        