n = int(input())# номер последней квартиры 
k = int(input())# квартира бабушки
c = int(input())# этажи в доме
kv = n*c #квартиры в доме
if k%kv == 0:
    pod = k//kv #pod - подъезд
else:
    pod = k//kv + 1
et = (k - (pod - 1) * kv) # - этаж
if et%n == 0:
    et = et//n
else:
    et = et//n + 1
print (pod,et)