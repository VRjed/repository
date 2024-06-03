print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                a = not(x <= z) or (y == w) or y
                if not a:
                    print(x,y,z,w,a)