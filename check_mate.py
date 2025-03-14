import pieces as p
import os

def clear_console():
    os_name = os.name
    if os_name == 'posix': # For macOS and Linux
        _ = os.system('clear')
    elif os_name == 'nt': # For Windows
        _ = os.system('cls')
    else:
        print("Operating system not supported for clearing the console.")

#Initialize empty board
board = p.Board()

#Initialize Players
player1 = p.Player
player2 = p.Player

#Populate board with pieces
minus_pawns = []
for i in range(0, 8):
    pawn= p.MinusPawn()
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
minusQueen = p.MinusQueen()
minus_queen.append(str(minusQueen))

minus_king = []
minusKing = p.MinusKing()
minus_king.append(str(minusKing))

starting_row_a = [minus_rooks[0], minus_knights[0], minus_bishops[0], minus_queen[0], minus_king[0], minus_bishops[1], minus_knights[1], minus_rooks[1]]

plus_pawns = []
for i in range(0, 8):
    pawn= p.PlusPawn()
    plus_pawns.append(str(pawn))

plus_rooks = []
for i in range(0, 2):
    rook = p.PlusRook()
    plus_rooks.append(str(rook))

plus_knights = []
for i in  range(0, 2):
    knight = p.PlusKnight()
    plus_knights.append(str(knight))

plus_bishops = []
for i in range(0, 2):
    bishop = p.PlusBishop()
    plus_bishops.append(str(bishop))

plus_queen = []
plusQueen = p.PlusQueen()
plus_queen.append(str(plusQueen))

plus_king = []
plusKing = p.PlusKing()
plus_king.append(str(plusKing))

starting_row_h = [plus_rooks[0], plus_knights[0], plus_bishops[0], plus_queen[0], plus_king[0], plus_bishops[1], plus_knights[1], plus_rooks[1]]

board.starting(minus_pawns, starting_row_a, plus_pawns, starting_row_h)

#Display welcome message
print("""\n\n\n===============    ============    =============         =====  =  =====       ==============    ===      =====       =======        ====
===============    ============    =============        =====  = =  =====      ==============    ===     ======     ===========      ====
    ======         ====            ====     ====       =====  == ==  =====          ====         ===    === ===    ====      ====    ====
    ======         =========       ====     ====      =====  === ===  =====         ====         ===   ===  ===    ====      ====    ====
    ======         =========       ===========        =====  === ===  =====         ====         ===  ===   ===    ==============    ====
    ======         ====            ============       =====  === ===  =====         ====         === ===    ===    ==============    ====
    ======         ============    =====   =====      =====  === ===  =====    ==============    =====      ===    ====      ====    ============
    ======         ============    =====     =====    =====  ==   ==  =====    ==============    ====       ===    ====      ====    ============

                                   ============    ====    ====    ============    ============    ============
                                   ============    ====    ====    ============    ============    ============
                                   ===             ====    ====    ====              =====           =====
                                   ===             ============    =========          =====           =====
                                   ===             ============    =========           =====           =====
                                   ===             ====    ====    ====                  =====           =====
                                   ============    ====    ====    ============    =============    ============
                                   ============    ====    ====    ============    =============    ============\n\n\n""")

j = input("Input 's' to start! ")
if j == 's':
    clear_console()

#Display starting board
print(board)
print('\n\n')

#Game Loop
while (board.location('+K+')[2] == True) and (board.location('-K-')[2] == True):

    player1.turn = "Yes"
    player2.turn = "No"

    if (player1.turn == "Yes") and (player2.turn =="No"):
        print("Player 1, it is your turn. Input 'y' to move. ")

    i = input("Player 1, it is your turn. Input 'y' to move. ")
    if i == "y":
        board.move()
        clear_console()
        print(board)
        print('\n\n')
        player1.turn = "No"

        if board.location('+K+') == False:
            print("Congratulations Player 1, you have won!")
            break
        else:
            pass

    player2.turn = "Yes"
    if (player2.turn == "Yes") and (player1.turn == "No"):
        print("Player 2, it is your turn. Input 'y' to move ")

    i = input("Player 2, it is your turn. Input 'y' to move. ")
    if i == "y":
        board.move()
        clear_console()
        print(board)
        print('\n\n')
        player2.turn = "No"

        if board.location('-K-') == False:
            print("Congratulations Player 2, you have won!")
            break
        else:
            pass
