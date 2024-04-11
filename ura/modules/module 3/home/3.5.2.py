a = set(input().upper())
b = ''
f =''
for i in range(26):
    b += chr(ord('A') + i) 
for i in a:
    if i not in b:
        continue
    else:
        f += i
b = list(f)
b.sort()
print(b)