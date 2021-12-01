import pygame
pygame.init()

tamanho = (800, 600)

tela = pygame.display.set_mode(tamanho)
boneco = pygame.image.load("mario.png")

executando = True

while executando:
    tela.fill((255, 255, 255))
    tela.blit(boneco, (5,3))
    
    pygame.display.flip()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
            

    