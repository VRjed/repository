res = {}
def game(x,y):
    if (x,y) in res:
        return res[(x,y)]
    if x+y >= 83:
        return 0
    moves = [game(x + 1,y), game(x *4,y),game(x,y + 1),game(x,y*4)]
    negat = [s for s in moves if s <= 0]
    if negat:
        temp = -max(negat) + 1
    else: 
        temp = -max(moves)
    res[(x,y)] = temp
    return temp
for i in range(77,0,-1):
    if game(5,i) == -2:
        print(i,game(5,i))
