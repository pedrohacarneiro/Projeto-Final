import pygame
pygame.init()

from parametros import *
from funcoes import *

LARGURA = 800
ALTURA = 600
jogo = True
tela_atual = "tela inicial"

TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Simpsons Subway Surfers")
while jogo:
    
    if tela_atual=="tela inicial":
        jogo, tela_atual = tela_inicial(jogo,TELA,fundo,titulo_rect,personagem,personagem_rect,tela_atual)
    if tela_atual == "tela jogo":
        jogo, tela_atual = tela_jogo(TELA)

pygame.quit()