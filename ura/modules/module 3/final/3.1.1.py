a = input()
b = set(a)
sp = list(b)
sp.sort()
for i in sp:
    print(i, a.count(i))