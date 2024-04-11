a = int(input())
num1 = a // 100
num2 = a // 10 % 10
num3 = a % 10
if a > 999 or a < 100:
    print("ошибка")
elif a % 100 == 0 or (num1 == num2 and num2 == num3 and num3 == num1):
    print("одно число")
elif num1 != num2 and num2 != num3 and num3 != num1 and (num1 == 0 or num2 ==0 or num3 == 0):
    print("четыре числа")
elif num1 != num2 and num2 != num3 and num3 != num1 and (num1 != 0 or num2 !=0 or num3 != 0):
    print("шесть чисел")
elif num1 == num2 or num2 == num3 or num3 == num1:
	print("три числа")

