b = 0
def count(st):
    b = 0
    glas = 'aeyuio'
    for i in st:
        if i in glas:
            b += 1
    return b 
da = input()
cb = count(da)
print(cb)