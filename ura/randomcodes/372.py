for i in range(10):
    a = 1 * int('12' + str(i) + '34') + 9
    b = 2 * int('1234' + str(i)) + 3
    if (a + b) % 10 == 0:
        print((a+b)//10)
    
        