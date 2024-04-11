text = input()
num = int(input())
b = len(text)
while b < num:
    if b + 2 > num:
        text = text + '.'
        break
    text = text[0] + text + text[-1]
    b = len(text)  
print(text)

