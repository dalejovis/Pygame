import pygame
from random import randint
pygame.init()
x1 = 365 #valor máximo à direita é 650 e à esquerda é 100
y1 = 450 #valor máximo abaixo é 450 e àcima é 20
x2 = 165
y2 = 800
x3 = 365
y3 = 300
x4 = 565
y4 = 300
timer = 0
tempo_segundo = 0

velocidade_outros = 40
fundo = pygame.image.load('background.png')
carro1 = pygame.image.load('carro1.png')
carro2 = pygame.image.load('carro2.png')
carro3 = pygame.image.load('carro3.png')
carro4 = pygame.image.load('carro4.png')

font = pygame.font.SysFont('arial black', 30)
texto = font.render("Time: ", True, (255,255,255), (0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (65,50)

#define o tamanho da janela
janela = pygame.display.set_mode((800,600))

#Define o nome da janela
pygame.display.set_caption("Top Gear 2021")

#Define o loop que mantém a janela aberta
janela_aberta = True
while janela_aberta : 
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    #Comandos de movimentação
        comandos = pygame.key.get_pressed()
    
        if comandos[pygame.K_RIGHT] and x1 <= 465:
            x1+= 200
        if comandos[pygame.K_LEFT] and x1 >= 265:
            x1-= 200   

    #randomização do aparecimento dos carros
    if (y2 >= 600) and (y3 >= 600) and (y4 >= 600):
        y2 = randint(-500, -50) 
        y3 = randint(-900, -500)
        y4 = randint(-1200, -700)

    #placar de pontuação
    if (timer <5):
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render("Points: "+str(tempo_segundo), True, (255,255,255), (0,0,0))
        timer = 0

    y2 += velocidade_outros + 5
    y3 += velocidade_outros + 10
    y4 += velocidade_outros + 30

    janela.blit(fundo, (0, 0))
    janela.blit(carro1, (x1, y1))
    janela.blit(carro2, (x2, y2))
    janela.blit(carro3, (x3, y3))
    janela.blit(carro4, (x4, y4))
    janela.blit(texto, pos_texto)

    pygame.display.update()
pygame.quit()