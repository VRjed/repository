def R(N):
    n2 = bin(N)[2:]
    if N % 6 == 0:
        n2 = str(n2.count("1") % 2) + n2 
    else:
        n2 += "0"
    if len(n2) % 2 == 0:
        n2 += "0"
    else:
        n2 += "1"
    n10 = int(n2, 2)
    return abs(N - n10)
a = []
for i in range(1, 1001):
    if R(i) > 2022:
        a.append(R(i))
new_n = hex(min(a))[2:]
s = 0
for x in new_n:
    s += int(x, 16)
print(s)









