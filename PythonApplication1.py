class ChessMan:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tag = '&'

class Board:
    def __init__(self):
        self.board = [ ['.']*8 for i in range(8)]

    def print_b(self):
        for i in self.board:
            print(*i)

    def enter_obj(self, chess_obj):
        if type(chess_obj) == ChessMan:
            print(self.board[chess_obj.x], '\n')
            print(self.board[chess_obj.x][chess_obj.y], '\n')
            self.board[chess_obj.x][chess_obj.y] = '&'