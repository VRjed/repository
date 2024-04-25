import sys
sys.set_int_max_str_digits(10000000)
#sys.set_int_max_str_digits(100000000000000000000000000000000000000000000000000000000000000)
def f(n):
    if n < 3:
        return n * 3
    if n > 2 and n % 2 == 0:
        return f(n -2) * f(n-1) - n
    if n > 2 and n % 2 != 0:
        return f(n -1) - f(n-2) + 2 * n
g = str(f(30))
print(g[-2], g[-1])