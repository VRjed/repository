alf = "ЕСАУЛ"
count = 0
for i1 in alf:
    for i2 in alf:
        for i3 in alf:
            for i4 in alf:
                for i5 in alf:
                    s = i1 + i2 + i3 + i4 + i5
                    if len(set(s)) == 5:
                        if s.count("ЕА") + s.count("АЕ") + s.count("АУ") + s.count("УА") + s.count("ЕУ")+ s.count("УЕ") == 0 :
                            count += 1
print(count)
#ЕА АЕ АУ УА УЕ ЕУ