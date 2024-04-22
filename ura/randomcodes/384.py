for i in range(10):
    a = 1 * int('132' + str(i) + '4') + 3
    b = 1 * int('13' + str(i)+'42',22)
    if abs(a - b) % 100 == 53:
        print(abs(a - b) // 100)
        