name = input().split()
num = list(map(int,input().split()))
d = {}
for i in range(len(num)):
    d[name[i]]=num[i]
for i in d:
    if d[i] >= 4:
        a = 'True'
        break
    else:
        a = "False"
print(a)
        