s = input()
num1 = int(input())
num2 = int(input())
b = len(s)
if b > num2:
	print("слишком длинно")
if b < num1:
	print("слишком коротко")
if num1<b<num2:
 	n = 2