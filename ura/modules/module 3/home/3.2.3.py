a = input()
f = ''
for i in range(len(a)):
    if i + 1 != len(a):
        if a[i] == ',' and a[i+1] != " ":
            f += a[i] + ' '
            continue
        if a[i] == '.' and a[i+1] != " ":
            f += a[i] + ' '
            continue
        else:
            f += a[i]
    else:
        f = f + a[i]
print(f)