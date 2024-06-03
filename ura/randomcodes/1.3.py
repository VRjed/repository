alf = 'АПРСУ'
c = 1
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    a = x1 + x2 + x3 + x4 + x5
                    if a.count('У') <= 1 and "АА" not in a:
                        print(c)
                    c += 1