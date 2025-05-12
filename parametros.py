import pygame

LARGURA = 800
ALTURA = 600

BRANCO = (255, 255, 255)
AMARELO = (255, 223, 0)
CINZA_ESCURO = (50, 50, 50)

fundo = pygame.image.load("Springfield.jpg")
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

botaojogar = pygame.image.load('BotaoJogar.png')
botaojogar = pygame.transform.scale(botaojogar,(250,125))
botaojogar_rect = botaojogar.get_rect(center=(400, 500))

personagem = pygame.image.load("Bart.png")
personagem_rect = personagem.get_rect(bottomright=(LARGURA-20, ALTURA))

fonte_titulo = pygame.font.SysFont("comicsansms", 60, bold=True)
titulo = fonte_titulo.render("Subway Simpsons", True, AMARELO)
titulo_rect = titulo.get_rect(center=(LARGURA / 2, 25))

fonte_botao = pygame.font.SysFont("comicsans", 40)