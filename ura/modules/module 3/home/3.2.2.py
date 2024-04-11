a = input()
c = ''
numbers = '123456789'
for i in a:
    if i in numbers:
        i = int(i)
        if i >= 1:
            i = i - 1
    i = str(i)
    c += i
print(c)
        