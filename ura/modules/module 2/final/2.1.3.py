Не решено

bull = 10000
cow = 5000
calf = 500
money = 100000
units = 100
countbull = 0
countcow = 0
countcalf = 0
while money - bull >= 0:
    countbull += 1
    money = money - bull
if money != 0:
    while money - cow >= 0:
        countcow += 1
        money = money - cow
if money != 0:
    while money - calf >= 0:
        countcalf += 1
        money = money - calf
if money != 0:
    print(-1)
    print(-1)
    print(-1)
else:
    print(countbull,countcow,countcalf)
