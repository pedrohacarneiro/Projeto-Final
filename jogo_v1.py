import pygame

pygame.init()

LARGURA = 800
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Simpsons Subway Surfers")

BRANCO = (255, 255, 255)
AMARELO = (255, 223, 0)
AZUL_CEU = (135, 206, 235)
CINZA_ESCURO = (50, 50, 50)

fonte_titulo = pygame.font.SysFont("comicsansms", 60, bold=True)
fonte_botao = pygame.font.SysFont("comicsans", 40)

# try:
#     fundo = pygame.image.load("imagens/fundo_springfield.png")
#     fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))
#     personagem = pygame.image.load("imagens/bart_skate.png")
# except:
#     fundo = pygame.Surface((LARGURA, ALTURA))
#     fundo.fill(AZUL_CEU)
#     personagem = pygame.Surface((200, 200))
#     personagem.fill(AMARELO)

def desenha_botao(texto, x, y, largura, altura, cor, cor_hover, acao=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x < mouse[0] < x + largura and y < mouse[1] < y + altura:
        pygame.draw.rect(TELA, cor_hover, (x, y, largura, altura))
        if click[0] == 1 and acao:
            acao()
    else:
        pygame.draw.rect(TELA, cor, (x, y, largura, altura))
    texto_formatado = fonte_botao.render(texto, True, BRANCO)
    TELA.blit(texto_formatado, (x + (largura - texto_formatado.get_width()) // 2,
                                y + (altura - texto_formatado.get_height()) // 2))

def iniciar_jogo():
    print("Jogo iniciado!")

def tela_inicial():
    rodando = True
    while rodando:
        # TELA.blit(fundo, (0, 0))
        titulo = fonte_titulo.render("Simpsons Subway Surfers", True, AMARELO)
        TELA.blit(titulo, ((LARGURA - titulo.get_width()) // 2, 50))
        # TELA.blit(personagem, (LARGURA//2 - 100, 150))
        desenha_botao("JOGAR", LARGURA//2 - 100, 450, 200, 60, CINZA_ESCURO, (70, 70, 70), iniciar_jogo)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    tela_inicial()