class ChessMan:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tag = '&'

class Board:
    def __init__(self):
        self.board = []
        with open('chess_board.txt') as board_set:  ### Читает из файла макет доски
            for line in board_set:
                self.board.append(line.split())


    def print_b(self):
        for i in self.board:
            print(*i)

    def enter_obj(self, chess_obj):
        if type(chess_obj) == ChessMan:
            print(self.board[chess_obj.x], '\n')
            print(self.board[chess_obj.x][chess_obj.y], '\n')
            self.board[chess_obj.x][chess_obj.y] = '&'

a=Board()
a.print_b()