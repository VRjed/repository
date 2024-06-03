f = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\repository\\ura\\EGe\\zadanie24\\24-j5.txt').readline()
f = f.replace('OCK','_')
c = 0
v = 0
for i in f:
    if i == '_' :
        c += 1
f = f.replace('ST_', '"')
for i in f:
    if i == '"':
        v += 1
print(c-v)