f = open('').readline()
alfb = 'WCN'
alfn = '123456789'
h = ''
max_h = ''
for i in range(0,len(f)-1):
    if i in alfb 
        h += i
        if len(max_h) < len(h):
            max_h = h
    else:
        h = ''
print(max_h,len(max_h))