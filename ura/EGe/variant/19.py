res = {}
def game(x):
    if x in res:
        return res[x]
    if x >= 190:
        return 0
    moves = [game(x + 5), game(x * 7)]
    negat = [s for s in moves if s <= 0]
    if negat:
        temp = -max(negat) + 1
    else:
        temp = -max(moves)
    res[x] = temp
    return temp
for i in range(189,0,-1):
    if game(i) == -2:
        print(i,game(i))