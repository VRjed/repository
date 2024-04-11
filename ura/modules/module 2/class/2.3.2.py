v = input()
s = "I Love Python!"
for i in s:
    if i == v:
        c = "буква найдена"
        break
    else:
        c = "буква не найдена"
print(c)