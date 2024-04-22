for i in range(10):
    a = 1 * int('1' + str(i) + '234')**2 + 1 * int('1' + str(i) + '234') + 2
    b = 1 * int('1' + str(i)+'243')**2 +  1 * int('1' + str(i) + '243') + 1
    if (a + b) % 15 == 0:
        print((a+b)//15)
        