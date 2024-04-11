s = 1
b = 0
while s <= 5:
    a = int(input())
    s += 1
    if a <= 0:
        print("Введите положительное число!")
        s -= 1
    else:
        b += a
print(b)