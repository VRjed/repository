n = int(input()) 
c = 0
for i in str(n):
    if int(i) // 10 == 1 or int(i) % 10 == 1:
        c += 1
print(c)