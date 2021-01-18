### Классы проекта
from lib import *

class ChessBoard:
    def __init__(self):
        self.board = []
        with open('chess_board.txt') as board_set:  ### Читает из файла макет доски
            for line in board_set:
                self.board.append(line.split())

class LOL:
    def __init__(self):
        pass