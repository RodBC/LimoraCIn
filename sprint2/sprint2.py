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
x_azul = choice(valores_para_x)
y_azul = 100
x_amarelo = 0
y_amarelo = 0

tela = pygame.display.set_mode((largura,altura))
relogio = pygame.time.Clock()
pygame.display.set_caption('LImo RaCIn')
fonte_padrao = pygame.font.get_default_font()
fonte = pygame.font.SysFont(fonte_padrao, 60, bold=False, italic=False)
texto = fonte.render(points_str, 1,(255,255,255))
carro1 = pygame.image.load('car_verde.png')
carro2 = pygame.image.load('car1_azul.png')

while True:
    relogio.tick(60)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a and x_verde >= 40:
                x_verde -= 10
            elif event.key == K_d and x_verde <= 560:
                x_verde += 10
            elif event.key == K_w and y_verde >= 10:
                y_verde -= 10
            elif event.key == K_s and y_verde <= 440:
                y_verde += 10


    if pygame.key.get_pressed()[K_a]:
        if(x_verde >= 10): x_verde -= 10
    elif pygame.key.get_pressed()[K_d]:
        if(x_verde <= 560): x_verde += 10
    elif pygame.key.get_pressed()[K_w]:
        if(y_verde >= 10): y_verde -= 10
    elif pygame.key.get_pressed()[K_s]:
        if(y_verde <= 440): y_verde += 10

    tela.blit(carro1,(x_verde,y_verde))
    tela.blit(carro2,(x_azul,y_azul))
    tela.blit(texto,(440,10))
    texto = fonte.render(points_str, 1,(255,255,255))
    y_azul += 4


    if y_azul > altura:
        y_azul = 0
        x_azul = randint(0,780)
    if y_amarelo > altura:
        y_amarelo = 0
        x_amarelo = randint(0,780)
    #confições de colisão
    #largura: 167
    #altura: 301
    if (x_verde + 167) > x_azul and (y_verde + 301) > y_azul:
        exit()
    '''if carro2.colliderect(rect_amarelo):
        points+=1
        print('Pontos: ',points)
        y_amarelo = 0
        x_amarelo = choice(valores_para_x)'''
    points_str = str(points)
    pygame

    pygame.display.update()