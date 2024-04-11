name = input().split()
num = list(map(int,input().split()))
d = {}
for i in range(len(num)):
    d[name[i]]=num[i]
if "Bob" in d:
    if d["Bob"] > 3:
        print("Fine")
    else:
        print("Help")
else:
    print("Bob is missing")
