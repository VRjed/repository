t = input()
sc1 = t.find('(')
sc2 = t.find(')') +1
print(t[:sc1] + t[sc2:])