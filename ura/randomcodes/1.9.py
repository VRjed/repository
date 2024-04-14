d = ''
for a in range(3,1001):
    k = 0
    i = '1' + a * '2'
    while '12' in i or '322' in i or '222' in i :
        if '12' in i:
            i = i.replace('12','2',1)
        if '322' in i:
            i = i.replace('322','21',1)
        if '222' in i:
            i = i.replace('222','3',1)
    
    
    
    
    
    
    
    
    
    
    d = d + ' ' + str(len(i))
    

    
print(max(d.split(' ')))
    