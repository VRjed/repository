f = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\repository\\ura\\randomcodes\\zadan24.1.txt').readline()
f = f.replace('A','_')
f = f.replace('B','_')
f = f.replace('C','_')
c = ''
mc = ''
for i in f:
    if i == '_':
        c += i
        if len(mc) < len(c):
            mc = c
    else:
        c = ''
print(len(mc),mc)
