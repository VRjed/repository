r = {}
def f(n):
    if n in r:
        return r[n]
    if n == 0:
        r[n] = 5
        return r[n]
    if n > 0:
        r[n] = 3 * f(n-4)
        return r[n]
    if n < 0:
        r[n] = f(n+3)
        return r[n] 
c = 0
for i in str(f(50)):
    c += int(i)
print(f(43))