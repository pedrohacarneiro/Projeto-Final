import pygame

pygame.init()

LARGURA = 800
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Simpsons Subway Surfers")

BRANCO = (255, 255, 255)
AMARELO = (255, 223, 0)
CINZA_ESCURO = (50, 50, 50)

fonte_titulo = pygame.font.SysFont("comicsansms", 60, bold=True)
fonte_botao = pygame.font.SysFont("comicsans", 40)

fundo = pygame.image.load("C:/Users/lucas/OneDrive/Insper/Design de Software/Py game/Projeto-Final/Springfield.jpg")
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))
personagem = pygame.image.load("C:/Users/lucas/OneDrive/Insper/Design de Software/Py game/Projeto-Final/Bart.png")

def desenha_botao(texto, x, y, largura, altura, cor, cor_clara, acao=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x < mouse[0] < x + largura and y < mouse[1] < y + altura:
        pygame.draw.rect(TELA, cor_clara, (x, y, largura, altura))
        if click[0] == 1 and acao:
            acao()
    else:
        pygame.draw.rect(TELA, cor, (x, y, largura, altura))
    texto_formatado = fonte_botao.render(texto, True, BRANCO)
    TELA.blit(texto_formatado, (x + (largura - texto_formatado.get_width()) // 2, y + (altura - texto_formatado.get_height()) // 2))

def iniciar_jogo():
    print("Jogo iniciado!") #so para funiconar (nao sei porque nao vai sem)

def tela_inicial():
    rodando = True
    while rodando:
        TELA.blit(fundo, (0, 0))
        titulo = fonte_titulo.render("Subway Simpsons", True, AMARELO)
        TELA.blit(titulo, ((LARGURA - titulo.get_width()) // 2, 15))
        TELA.blit(personagem, (LARGURA/1.33 - 100, 150))
        desenha_botao("JOGAR", LARGURA//2 - 100, 450, 200, 60, CINZA_ESCURO, (70, 70, 70), iniciar_jogo)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
        pygame.display.update()
    pygame.quit()

tela_inicial()