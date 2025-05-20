import pygame
pygame.init()
from parametros import *
from funcoes import *
pygame.mixer.init()

def main():
    jogo = True
    tela_atual = "tela inicial"

    TELA_INICIAL = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Springfield Surfers")

    contador = 0
    while jogo:
        if tela_atual == "tela inicial":
            jogo, tela_atual, contador = tela_inicial(
                jogo, 
                TELA_INICIAL,
                fundo, 
                titulo, 
                titulo_rect, 
                personagem, 
                personagem_rect, 
                botaojogar, 
                botaojogar_rect, 
                tela_atual,
                contador
            )
        elif tela_atual == "tela jogo":
            TELA_JOGO = pygame.display.set_mode((WIDTH, HEIGHT))
            jogo, tela_atual, contador = tela_jogo(TELA_JOGO, contador)
            if tela_atual == "tela inicial":
                TELA_INICIAL = pygame.display.set_mode((LARGURA, ALTURA))

    pygame.quit()

if __name__ == "__main__":
    main()