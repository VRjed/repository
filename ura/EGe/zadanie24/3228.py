f = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\repository\\ura\\EGe\\zadanie24\\24_3228.txt').readline()
f = f.replace('AC','_')
f = f.replace('AB','_')
h = ''
mh = ''
for i in f:
    if i == '_':
        h += i
        if len(mh) < len(h):
            mh = h
    else:
        h = ''
print(len(mh),mh)