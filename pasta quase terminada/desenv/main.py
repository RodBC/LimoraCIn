import pygame
from pygame.locals import *
from sys import exit
from random import randint,choice

pygame.init()
valores_para_x = [30,50,70,100] #valores fixos que representam a faixa em que os carros vão aparecer
points = 0
points_str = str(points)
largura = 780
altura = 600
x_verde = largura/2
y_verde = altura/2
x_azul = randint(140, 629)
y_azul = -100
x_amarelo = 0
y_amarelo = 0
x_pitu = randint(140, 629)
y_pitu = -80
flag_soma = 4

tela = pygame.display.set_mode((largura,altura))
relogio = pygame.time.Clock()
pygame.display.set_caption('LImo RaCIn')
fonte_padrao = pygame.font.get_default_font()
fonte = pygame.font.SysFont(fonte_padrao, 60, bold=False, italic=False)
texto = fonte.render(points_str, 1,(255,255,255))
carro_verde = pygame.image.load('../imagens/greenCar.png')
carro_azul = pygame.image.load('../imagens/blueCar.png')
pitu = pygame.image.load('../imagens/pitu.png')
background = pygame.image.load('../imagens/fundo.png')	

while True:
    relogio.tick(60)
    tela.fill((0, 0, 0))
    tela.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a and x_verde >= 140:
                x_verde -= 10
            elif event.key == K_d and x_verde <= 629:
                x_verde += 10
            elif event.key == K_w and y_verde >= 10:
                y_verde -= 10
            elif event.key == K_s and y_verde <= 450:
                y_verde += 10

    #Define a movimentação do carro verde, respeitando os limites da estrada da imagem de fundo
    if pygame.key.get_pressed()[K_a]:
        if(x_verde >= 140): x_verde -= 7
    elif pygame.key.get_pressed()[K_d]:
        if(x_verde <= 629): x_verde += 7
    elif pygame.key.get_pressed()[K_w]:
        if(y_verde >= 10): y_verde -= 7
    elif pygame.key.get_pressed()[K_s]:
        if(y_verde <= 450): y_verde += 7

    #Coloca os objetos na tela
    tela.blit(carro_verde,(x_verde,y_verde))
    tela.blit(carro_azul,(x_azul,y_azul))
    tela.blit(pitu,(x_pitu,y_pitu))
    tela.blit(texto,(440,10))
    texto = fonte.render(points_str, 1,(255,255,255))
    y_azul += flag_soma #lembrar de colocar flag para aumentar a velocidade
    y_pitu += 6

    #Condicionao para que, se os objetos interativos passarem do limite inferior, volta para cima
    if y_azul > altura:
        y_azul = -100
        x_azul = randint(160,629)
    if y_pitu > altura:
        y_pitu = -80
        x_pitu = randint(160,629)

    if y_verde < (y_azul + 120):
        if y_verde < y_azul - 150:
            pass
        else:
            if (x_verde > x_azul and x_verde < (x_azul + 55)) or ((x_verde + 55) > x_azul and (x_verde + 55) < (x_azul + 55)):
                exit()

    if y_verde < (y_pitu + 71):
        if y_verde < y_pitu - 150:
            pass
        else:
            if (x_verde > x_pitu and x_verde < (x_pitu + 65)) or ((x_verde + 75) > x_pitu and x_verde < x_pitu):
                y_pitu = -80
                x_pitu = randint(160,629)
                flag_soma += 0.7

    pygame.display.update() 