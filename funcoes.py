import pygame
from parametros import *

def tela_inicial(jogo, TELA,fundo,titulo_rect,personagem,personagem_rect,tela_atual):
    TELA.blit(fundo, (0, 0))
    TELA.blit(titulo, titulo_rect)
    TELA.blit(personagem, personagem_rect)
    TELA.blit(botaojogar, botaojogar_rect)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo = False

    pygame.display.update()

    return jogo, tela_atual

def tela_jogo(TELA):
    rodando = True
    TELA.fill((255, 255, 255))
    pygame.display.update()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    return rodando, "tela jogo"