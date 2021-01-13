from lib import *
from classes import *

white,black,red = (255,255,255),(0,0,0),(255,0,0)

def printChessTemplate(chess_board, gameDisplay):
    for i in range(len(chess_board.board)):
        print(chess_board.board[i])
        #for j in i:
        #    if j == 'w':
        #        pygame.draw.rect(gameDisplay, white, [x+40*j,y+40*i,20,20])
        #    else:
        #        pygame.draw.rect(gameDisplay, red, [x+40*j,y+40*i,20,20])
    



def main():
    pygame.init()

    gameDisplay = pygame.display.set_mode((800,600))

    pygame.display.set_caption("ChessBoard")
    gameExit = True

    board = ChessBoard() ### Создаёт объект шахматной доски (ChessBoard берет из classes.py)
    printChessTemplate(board, gameDisplay) ### Выводит в консоль сам макет из файла


    x = 20
    y = 20

    while  gameExit==True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = False
            gameDisplay.fill(black)
            
            for i in range(4):
                for j in range(4):
                    pygame.draw.rect(gameDisplay, white, [x+40*j,y+40*i,20,20])
            pygame.display.update()
            pygame.display.flip()


    pygame.quit()

if __name__ == '__main__':
    main()