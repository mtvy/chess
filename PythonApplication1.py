class color(object):
    em=0
    white=2
    black=1
class ChessMan(object):
    IMG=None
    def __init__(self,color):
        self.color=color
    def __repr__(self):
        return self.IMG[self.color]
class Pawn(ChessMan):
        IMG=('♙','♟')
        def get_moves(self,board,x,y):
            moves=[]
            retirn moves 

class King(ChessMan):
    IMG=('♔','♚')
class Rook(ChessMan):
    IMG=('♖','♜')
class Bishops(ChessMan):
    IMG=('♗','♝')
class Knigts (ChessMan):
    IMG=('♘','♞')
class Queen(ChessMan):
    IMG=('♕','♛')
class Board(object):
    def __init__(self):
        self.board=[['.']*8 for i in range (8)]
        for i in range (8):
            self.board[1][i]=Pawn(1)
        for i in range (8):
            self.board[6][i]=Pawn(0)
        self.board[0][4]=King(1)

    def __repr__(self):
        res= ''
        for y in range (8):
            res+=''.join(map(str,self.board[y]))+"\n"
        return res
     
print(Board())