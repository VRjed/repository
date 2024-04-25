def f(n):
    if n < 4:
        return n-1
    if n >= 4 and n % 3 == 0:
        return n + 2 * f(n-1)
    if n >= 4 and n % 3 != 0:
        return f(n-2)+f(n-3)
c = 0
for i in str(f(25)):
    c += int(i)
print(c)