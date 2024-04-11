a = int(input())
s = 0
for i in range(a+100):
    s += i
    if i == a:
        print(s)   