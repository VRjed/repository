f = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\repository\\ura\\EGe\\zadanie24\\24-1.txt').readline()
h = ''
max_h = ''
for i in f:
    if i in '13579':
        h += i
        if len(max_h) < len(h):
            max_h = h
    else:
        h = ''
print(max_h)