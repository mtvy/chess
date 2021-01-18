import pygame
pygame.init()

white,black,red = (255,255,255),(0,0,0),(255,0,0)

gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption("ChessBoard")
gameExit = True

while  gameExit==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = False
    gameDisplay.fill(white)
    for i in range (4):
        for j in range(4):
           pygame.draw.rect(gameDisplay,black,(0+40*i,0+40*j,20,20))
    for i in range (4):
        for j in range(4):
             pygame.draw.rect(gameDisplay,black,(20+40*i,20+40*j,20,20))
   
    pygame.draw.line(gameDisplay,black,(0,0),(0,160),3)
    pygame.draw.line(gameDisplay,black,(0,160),(160,160),3)
    pygame.draw.line(gameDisplay,black,(160,160),(160,0),3)
    pygame.draw.line(gameDisplay,black,(0,0),(160,0),3)
    pygame.display.update()
    pygame.display.flip()
   
pygame.quit()
