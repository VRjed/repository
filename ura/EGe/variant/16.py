def f(n):
    if n > 3456:
        return 3*n+1
    if n < 3456:
        return n - 10 + f(n + 10)
print(f(3425) + f(3430))