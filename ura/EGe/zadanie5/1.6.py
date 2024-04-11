for N in range(1, 1000):
    n = N
    result = ""
    while n > 0:
        result += str(n % 3)
        n //= 3
    n3 = result[::-1]
    if N % 3 == 0:
        n3 += n3[-3:]
    else:
        m = N % 3 * 3 
        result = ""
        while m > 0:
            result += str(m % 3)
            m //= 3
        m3 = result[::-1]
        n3 += m3
    R = int(n3, 3)
    if R > 340:
        print(N)
        break