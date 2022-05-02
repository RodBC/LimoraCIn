import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

altura = 600
largura = 480
x_verde = 0
y_verde = 0
x_vermelho = 100
y_vermelho = 100

tela = pygame.display.set_mode((altura,largura))
relogio = pygame.time.Clock()
pygame.display.set_caption('LImo RaCIn')

while True:
    relogio.tick(60)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                x_vermelho -= 10
            elif event.key == K_d:
                x_vermelho += 10
            elif event.key == K_w:
                y_vermelho -= 10
            elif event.key == K_s:
                y_vermelho += 10


    if pygame.key.get_pressed()[K_a]:
        x_vermelho -= 10
    elif pygame.key.get_pressed()[K_d]:
        x_vermelho += 10
    elif pygame.key.get_pressed()[K_w]:
         y_vermelho -= 10
    elif pygame.key.get_pressed()[K_s]:
        y_vermelho += 10

    rect_verde = pygame.draw.rect(tela,(0,135,1),(x_verde,y_verde,30,30))
    rect_vermelho = pygame.draw.rect(tela,(255,0,0),(x_vermelho,y_vermelho,30,30))
    y_verde += 4

    if y_verde > altura:
        y_verde = 0
        x_verde = randint(50,350)
    if rect_verde.colliderect(rect_vermelho):
        pygame.quit()
        exit()
    pygame.display.update()