f = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\repository\\ura\\EGe\\zadanie24\\24-264.txt').readline()
alf = '0123456789ABCDEF'
h = ''
mh = ''
for i in f:
    if i in alf:
        h += i
        if len(mh) < len(h):
            mh = h
    else:
        h = ''
print(len(mh),mh)