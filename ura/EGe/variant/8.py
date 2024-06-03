alf = '0123456'

c = 0
for x1 in alf[1:]:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    a = x1 + x2 + x3 + x4 + x5
                    if a.count('2') == 0:
                        d = {}
                        for i in a:
                            if i in d:
                                d[i] += 1
                            else:
                                d[i] = 1
                        if len(d) == 5:
                            if  '04' not in a and '06' not in a and '40' not in a and '46' not in a and '60' not in a and '64' not in a and '13' not in a and '15' not in a and '31' not in a and '35' not in a and '51' not in a and '53' not in a:
                                c += 1
print(c)