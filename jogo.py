import pygame
pygame.init()
from parametros import *
from funcoes import *

def main():
    # Configurações iniciais
    jogo = True
    tela_atual = "tela inicial"

    # Telas - cada uma com suas próprias dimensões
    TELA_INICIAL = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Springfield Surfers")

    # Loop principal do jogo
    while jogo:
        if tela_atual == "tela inicial":
            jogo, tela_atual = tela_inicial(
                jogo, 
                TELA_INICIAL,  # Usando apenas TELA_INICIAL aqui
                fundo, 
                titulo, 
                titulo_rect, 
                personagem, 
                personagem_rect, 
                botaojogar, 
                botaojogar_rect, 
                tela_atual
            )
        elif tela_atual == "tela jogo":
            # Criamos a tela de jogo apenas quando necessário
            TELA_JOGO = pygame.display.set_mode((WIDTH, HEIGHT))
            jogo, tela_atual = tela_jogo(TELA_JOGO)
            # Quando sair do jogo, voltamos para a tela inicial
            if tela_atual == "tela inicial":
                TELA_INICIAL = pygame.display.set_mode((LARGURA, ALTURA))

    pygame.quit()

if __name__ == "__main__":
    main()