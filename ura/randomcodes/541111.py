def f(n):
    if n > 25:
        return 2 * n*n*n + n*n
    if n <=25:
        return f(n+2) + 2 * f(n+3)
c = 0
for i in str(f(2)):
    c += int(i)
print(c)