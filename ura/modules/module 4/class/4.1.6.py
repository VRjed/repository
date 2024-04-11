def div(number):
    k = 2 
    for i in range(2, number):
        if number % i == 0:
            k += 1 
    return k