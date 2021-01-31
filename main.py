import pygame
from classes import *
from const import *

def main():
    pygame.init()

    gameDisplay = pygame.display.set_mode((360,360))

    pygame.display.set_caption("ChessBoard")
    gameExit = True

    a = Board()
    a.print_b()


    while  gameExit==True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = False
        gameDisplay.fill(TESTING_COLOR)
        for i in range (8):
            for j in range(8):
                if a.board[i][j] == 'w':
                    pygame.draw.rect(gameDisplay, WHITE,(20+i*40,20+j*40,40,40))
                if a.board[i][j] == 'b':
                    pygame.draw.rect(gameDisplay,BLACK,(20+i*40,20+j*40,40,40))

        pygame.draw.line(gameDisplay,RED,(16,15),(16,340),4)
        pygame.draw.line(gameDisplay,RED,(16,340),(340,340),4)
        pygame.draw.line(gameDisplay,RED,(340,340),(340,16),4)
        pygame.draw.line(gameDisplay,RED,(16,16),(340,16),4)
        pygame.display.update()
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
