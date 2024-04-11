s = 1
b = 1
while s <= 6:
    a = int(input())
    s += 1
    if a % 2 != 0:
        print("Введите четное число!")
        s -= 1
    else:
        b *= a
print(b)