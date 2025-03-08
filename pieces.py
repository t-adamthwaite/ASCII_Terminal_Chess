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

    def state(self):
        return str(self.row0) + '\n\n' + str(self.rowA) + '\n\n' + str(self.rowB) + '\n\n' + str(self.rowC) + '\n\n' + str(self.rowD) + '\n\n' + str(self.rowE) + '\n\n' + str(self.rowF) + '\n\n' + str(self.rowG) + '\n\n' + str(self.rowH)
    
    def starting(self):
        self.rowA["A"] = ['-R-', '-N-', '-B-', '-Q-', '-K-', '-B-', '-N-', '-R-']
        for i in range (0, 8):
            self.rowB["B"][i] = '-P-'
        for i in range (0, 8):
            self.rowG["G"][i] = '+P+'
        self.rowH["H"] = ['+R+', '+N+', '+B+', '+Q+', '+K+', '+B+', '+N+', '+R+']