a = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\repository\\ura\\EGe\\zadanie26\\26-j9.txt')
f,b = map(int,a.readline().split())
h = list(map(int,a.readlines()))
h.sort()
c = 0
d = []
while f >= min(h) + max(h):
    f = f - (min(h) + max(h))
    c += 2
    h.remove(min(h))
    h.remove(max(h))
    d.append(min(h))
    d.append(max(h))
print(c)
print(f)
print(h)

573
229
