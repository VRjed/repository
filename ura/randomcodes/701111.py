r = {}
def f(n):
    if n in r:
        return r[n]
    if n == 0:
        r[n] = 1
        return r[n]
    if n > 0:
        r[n] = 2 * f(1-n) + 3 * f(n-1)+2
        return r[n]
    if n < 0:
        r[n] = -f(-n)
        return r[n] 
c = 0
for i in str(f(50)):
    c += int(i)
print(c)