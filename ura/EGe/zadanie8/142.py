alf = "ВАЯЮЩИЙ"
count = 0
for i1 in alf:
    for i2 in alf:
        for i3 in alf:
            for i4 in alf:
                s = i1 + i2 + i3 + i4
                if i1 != 'Й':
                    if s.count('Я') >= 1 or s.count('И') >= 1 or s.count('А') >= 1 or s.count('Ю') >= 1:
                        count += 1
print(count)

