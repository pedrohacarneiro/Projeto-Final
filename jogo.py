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
    contador=0
    while jogo:
        if tela_atual == "tela inicial":
            jogo, tela_atual,contador = tela_inicial(
                jogo, 
                TELA_INICIAL,  # Usando apenas TELA_INICIAL aqui
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
        elif tela_atual == "como jogar":
            jogo, tela_atual = tela_comojogar(jogo, TELA_INICIAL, comojogar_imagem)
        elif tela_atual == "tela jogo":
            # Criamos a tela de jogo apenas quando necessário
            TELA_JOGO = pygame.display.set_mode((WIDTH, HEIGHT))
            jogo, tela_atual,contador = tela_jogo(TELA_JOGO,contador)
            # Quando sair do jogo, voltamos para a tela inicial
            if tela_atual == "tela inicial":
                TELA_INICIAL = pygame.display.set_mode((LARGURA, ALTURA))

    pygame.quit()

if __name__ == "__main__":
    main()

