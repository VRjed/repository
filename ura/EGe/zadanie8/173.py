alf = "ЕЛЙ"
count = 0
for i1 in alf:
    for i2 in alf:
        for i3 in alf:
            for i4 in alf:
                for i5 in alf:
                    for i6 in alf:
                        s = i1 + i2 + i3 + i4 + i5 + i6
                        if i1 != 'Й' and i6 != 'Й' :
                            if s.count('Й')  <= 1:
                                if ('ЙЕ' and "ЕЙ") not in s:
                                    count += 1
print(count)
#23625