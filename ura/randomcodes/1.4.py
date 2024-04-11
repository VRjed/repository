alf = 'АВИОРТФ'
count = 0
for i1 in alf:
    for i2 in alf:
        for i3 in alf:
            for i4 in alf:
                for i5 in alf:
                     for i6 in alf:
                        c = i1 + i2 + i3 + i4 + i5 + i6
                        if c[0] != 'О':
                            if c.count('Р') == 2:
                                count += 1
print(count ,' \\\\')
                            