import pygame
def main():
    pygame.init()

    white,black,red = (255,255,255),(0,0,0),(255,0,0)

    gameDisplay = pygame.display.set_mode((800,600))

    pygame.display.set_caption("ChessBoard")
    gameExit = True

    x = 20
    y = 20

    while  gameExit==True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = False
            gameDisplay.fill(BLACK)
            for i in range(4):
                for j in range(4):
                    pygame.draw.rect(gameDisplay, WHITE, [x+40*j,y+40*i,20,20])
            pygame.display.update()
            pygame.display.flip()


    pygame.quit()
if __name__ == '__main__':
    main()