alf = '012345678'
c = 0
for x1 in alf[1:]:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    for x6 in alf:
                        a = x1 + x2 + x3 + x4 + x5 + x6
                        if a.count('1') == 0 and a.count('3') == 0:
                            d = {}
                            for i in a:
                                if i in d:
                                    d[i] += 1
                                else:
                                    d[i] = 1
                            if len(d) == 6:
                                if '03' not in a and '06' not in a and '30' not in a and '36' not in a and '60' not in a and '63' not in a:
                                    c += 1
print(c)