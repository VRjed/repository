a = int(input())
b = int(input())
c = int(input())
h = 1
if a < b:
    h = 0
else:
    for i in range(a+1):
        g = a - b + c
        a = g 
        if a < b:
            break
        else:
            h += 1
print(h)

