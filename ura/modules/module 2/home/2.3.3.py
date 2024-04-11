g = input()
b = 0
h = 0
glas = 'AEOUYI'
for i in g:
    if i in glas:
        b += 1
    else:
        h += 1
print(b,h)