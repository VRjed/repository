num1 = int(input())
num2 = int(input())
if num1 % 2 != 0 and num2 % 2 != 0:
    c = "Оба нечетные"
if num1 % 2 == 0:
    c = "Первое четное"
if num2 % 2 == 0:
    c = "Второе четное" 
if num1 % 2 == 0 and num2 % 2 == 0:
    c = "Оба четные"
print (c)