a = set(input().split(' '))
a = list(a)
a.sort()
f = ''
for i in a:
    if len(f) > len(i):
        continue
    else:
        f = i
print(f)   
