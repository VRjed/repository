s = 1
b = 1
while s != 0:
    a = int(input())
    s = a
    if a < 0:
        print("Введите положительное число!")
    else:
        if a == 0:
            a = 1
        b *= a
print(b)