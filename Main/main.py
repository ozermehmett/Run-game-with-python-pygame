import pygame, sys
from sprites import PLAYER


pygame.init()
WHITE = (255,255,255)
W, H = 900, 600
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

font = pygame.font.SysFont('Comic Sans MS', 24)
text = font.render("Text", True, (255, 255, 255))

player = PLAYER(W, H)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.update()

    player.run()    
    screen.fill((150,150,0))
    player.engel()
    player.draw(screen)
    pygame.display.update()

    clock.tick(30)
