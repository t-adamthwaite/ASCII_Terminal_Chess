class Board:

    def __init__(self, row0 = {}, rowA = {}, rowB = {}, rowC = {}, rowD = {}, rowE = {}, rowF = {}, rowG = {}, rowH = {}):
        self.row0 = {" ": ['_1_', '_2_', '_3_', '_4_', '_5_', '_6_', '_7_', '_8_']}

        self.rowA = {"A": ['___', '___', '___', '___', '___', '___', '___', '___']}
    
        self.rowB = {"B": ['___', '___', '___', '___', '___', '___', '___', '___']}

        self.rowC = {"C": ['___', '___', '___', '___', '___', '___', '___', '___']}

        self.rowD = {"D": ['___', '___', '___', '___', '___', '___', '___', '___']}

        self.rowE = {"E": ['___', '___', '___', '___', '___', '___', '___', '___']}

        self.rowF = {"F": ['___', '___', '___', '___', '___', '___', '___', '___']}

        self.rowG = {"G": ['___', '___', '___', '___', '___', '___', '___', '___']}

        self.rowH = {"H": ['___', '___', '___', '___', '___', '___', '___', '___']}

    def __str__(self):
        return str(self.row0) + '\n\n' + str(self.rowA) + '\n\n' + str(self.rowB) + '\n\n' + str(self.rowC) + '\n\n' + str(self.rowD) + '\n\n' + str(self.rowE) + '\n\n' + str(self.rowF) + '\n\n' + str(self.rowG) + '\n\n' + str(self.rowH)
    
    def starting(self, minus_pawns):
        self.rowA["A"] = ['-R-', '-N-', '-B-', '-Q-', '-K-', '-B-', '-N-', '-R-']
        self.rowB["B"] = minus_pawns
        for i in range (0, 8):
            self.rowG["G"][i] = '+P+'
        self.rowH["H"] = ['+R+', '+N+', '+B+', '+K+', '+Q+', '+B+', '+N+', '+R+']

    def location(self, piece_id):
        piece_id = piece_id
        board_dict = self.rowA | self.rowB | self.rowC | self.rowD | self.rowE | self.rowF | self.rowG | self.rowH
        #if piece_id in board_dict.values():
        for key, list in board_dict.items():
            for item in list:
                if item == piece_id:
                    print("Piece is located in Row {CHAR}, column {NUM}.".format(CHAR = key, NUM = list.index(item)+1))
                    return True
        #else:
          #  print("Piece not on board.")


class MinusPawn:
    pawn_count = 0
    text = '-P'
    def __init__(self, first_move = False):
        MinusPawn.pawn_count += 1
        self.id = MinusPawn.text + str(MinusPawn.pawn_count)
        self.first_move = first_move
    
    def __str__(self):
        return self.id
    
    def move(self):
        piece_id = input(["Piece id: "])
        if Board.location(piece_id) == True:
            print('hello')

