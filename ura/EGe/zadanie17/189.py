def f(x):
    s = ""
    while x>0:
        s = str(x%3) + s
        x //= 3
c = 0
mn = 0
a = list(map(int, open('C:\\Users\\VR1\\Desktop\\repository\\repository\\ura\\EGe\\zadanie17\\17-7.txt').readlines()))
for i in range(0, len(a) - 2):    
    if (f(a[i]))[-1] == '2' or (f(a[i+1]))[-1] == '2' or (f(a[i+2]))[-1] == '2':
        c += 1
        mn += min(a[i],a[i+1],a[i+2])
print(c,mn)
