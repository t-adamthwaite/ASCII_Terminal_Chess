import pieces as p

#Initialize empty board
board = p.Board()

#Populate board with pieces
minus_pawns = []
for i in range(0, 8):
    pawn = p.MinusPawn()
    minus_pawns.append(str(pawn))

minus_rooks = []
for i in range(0, 2):
    rook = p.MinusRook()
    minus_rooks.append(str(rook))

minus_knights = []
for i in  range(0, 2):
    knight = p.MinusKnight()
    minus_knights.append(str(knight))

minus_bishops = []
for i in range(0, 2):
    bishop = p.MinusBishop()
    minus_bishops.append(str(bishop))

minus_queen = []
queen = p.MinusQueen()
minus_queen.append(str(queen))

minus_king = []
king = p.MinusKing()
minus_king.append(str(king))

starting_row_a = [minus_rooks[0], minus_knights[0], minus_bishops[0], minus_queen[0], minus_king[0], minus_bishops[1], minus_knights[1], minus_rooks[1]]

board.starting(minus_pawns, starting_row_a)

#Display current board
print((board))
#print(str(board.rowA["A"][0]))

#board.move()
#print(str(board))

#board.move()

#print(str(board))
#print(board)
