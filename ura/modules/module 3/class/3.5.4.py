a = int(input())
g = set()
count = set()
for i in range(a):
    n = input()
    if n not in g:
        g.add(n)
    else:
        count.add(n)
print(len(count))
