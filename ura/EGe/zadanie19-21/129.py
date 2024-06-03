res = {}
def game(x,y):
    if (x,y) in res:
        return res[(x,y)]
    if x**2 + y**2 >= 14**2:
        return 0
    moves = [game(2*x,y),game(x,y+3),game(x,y+4)]
    negat = [s for s in moves if s <=0]
    if negat:
        temp = -max(negat) + 1
    else:
        temp = -max(moves)
    res[(x,y)] = temp
    return temp
for i in range(13,0,-1):
    if game(3,i) == -2:
        print(i,game(3,i))