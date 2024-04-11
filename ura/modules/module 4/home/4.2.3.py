def calc_tiles(size,form = 'A4'):
    formate = {'A4':(165, 255),
    "A5": (80, 130)}
    if form in formate:
        f = (formate[form])[0] // size[0]
        g = (formate[form])[1] // size[1]
    else:
        f = form[0] // size[0]
        g = form[1] // size[1]
    return f * g

