m = int(input()) - 1
n = int(input()) 
h = ''
for i in range(1040, 1072):
    h += chr(i)
    if i == 1045:
        h = h + 'Ё'
        i = i - 1
        continue
print(h[m:n])

