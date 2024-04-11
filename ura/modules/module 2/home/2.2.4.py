a = int(input())
b = int(input())
c = int(input())
g = input()
v = "жёлтый"
if g == v and (((a + b) % 3)==0 or ((b+a) % 3) ==0 or ((c+a) % 3) == 0):
    print("ДА")
else:
    print("НЕТ")