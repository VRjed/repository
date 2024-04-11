alf = "КАЛЬ"
count = 0
for i1 in alf:
    for i2 in alf:
        for i3 in alf:
            for i4 in alf:
                for i5 in alf:
                    s = i1 + i2 + i3 + i4 + i5
                    if s.count("А") <= 1:
                        count += 1
print(count)
        