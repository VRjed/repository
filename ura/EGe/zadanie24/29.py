f = open('C:\\Users\\VR1\\Desktop\\repository\\repository\\repository\\ura\\EGe\\zadanie24\\k7b-3.txt').readline()
f = f.replace('BAFE','_')
h = ''
max_h = ''
for i in f:
    if i in "_" or i in 'BAF' or i in 'BA' or i in 'B':
        if i in '_':
            h += 'BAFE'
        else:
            h += i
        if len(max_h) < len(h):
           max_h = h 
    else:
        h = ''
print(len(max_h),max_h)
