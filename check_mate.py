import pieces as p

#Initialize empty board
board = p.Board()

#Populate board with pieces
minus_pawns = []
for i in range(0, 8):
    pawn = p.MinusPawn()
    minus_pawns.append(str(pawn))

board.starting(minus_pawns)

#Display current board
#print(str(board))
#print(str(board.rowA["A"][0]))

#board.location("-P3")

