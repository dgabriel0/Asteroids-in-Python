# the beginning
import pygame
# tamanho da largura e altura da tela 
sw = 800
sh = 600

# importando as imagens
chick = pygame.image.load("assets/chick.png")
background = pygame.image.load("assets/background.png")
ship = pygame.image.load("assets/ship.png")
banner = pygame.image.load("assets/BANNER.png")
shoot = pygame.image.load("assets/shoot.png")


pygame.display.set_caption('chick invasion')
win = pygame.display.set_mode((sw,sh))
# att de tela 
clock = pygame.time.Clock()

gameover = False

def redrawGameWindow():
    win.blit(background,(0,0))
    pygame.display.update()


run = True

while run:
    clock.tick(60)
    if not gameover:
        pass


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redrawGameWindow()        

pygame.QUIT()