t = input()
tochka = t.rfind('.') + 1
s = t[tochka:]
if len(t[tochka:]) == t[tochka:].count(" "):
	print('Ok')
else:
	print('Лишние символы!')
