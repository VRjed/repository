alf = "АРЕЛ"
count = 0
for i1 in alf:
    for i2 in alf:
        for i3 in alf:
            for i4 in alf:
                for i5 in alf:
                    s = i1 + i2 + i3 + i4 + i5
                    if s.count("А") == 2 and s.count("Е") == 1 and s.count("Р") == 1 and s.count("д") == 1:
                        if s.count("ЕА") + s.count("АЕ") + s.count("АА")  == 0 :
                            count += 1
print(count
#АА АЕ ЕА УА УЕ ЕУ