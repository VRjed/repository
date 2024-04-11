text = input()
a = ''
while a != 'стоп':
    g = input()
    if g == 'стоп':
        break
    g = int(g)
    print(text[g])