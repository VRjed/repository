res = {}
def game(x):
    if x in res:
        return res[x]
    if x >= 33:
        return 0
    moves = [game(x + 3), game(x * 2)]
    negat = [s for s in moves if s <= 0]
    if negat:
        temp = -max(negat) + 1
    else:
        temp = -max(moves)
    res[x] = temp
    return temp
for i in range(32,0,-1):
    if game(i) == -2:
        print(i,game(i))

