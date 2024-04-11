s = 1
h = 1
b = 0
m = 10
count = 0
while s != 0:
    a = int(input())
    if a == 0:
        break
    s = a
    count += 1
    b += a
    if h > a:
        h = h   
    else:
        h = a
    if m < a:
        m = m
    else:
        m = a
d = b/count
print(count,m,h,b,d)