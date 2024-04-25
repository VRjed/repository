r = {}
def f(n):
    if n <= 1:
        r[n] = 1
        return r[n]
    if n > 1 and n % 2 == 0:
        r[n] = n + f(n-1)
        return r[n]
    if n > 1 and n % 2 != 0:
        r[n] = n * n + f(n-2)
        return r[n]
print(f(80))