a = int(input()) 
s = 0
for i in range(a + 1):
    if i == 1:
        s = 1
    else:
        s = s + (i + (i - 1))
print(s)