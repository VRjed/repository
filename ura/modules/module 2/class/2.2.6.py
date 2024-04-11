a = int(input())
b = int(input())
c = b - 100
if a == c:
    print("Вес оптимален")
if a > c:
    print("Вам надо похудеть на",a - c,"кг")
if a < c:
    print("Вам надо поправиться на",-a + c,"кг")