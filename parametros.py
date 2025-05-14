# import pygame

# LARGURA = 800
# ALTURA = 600

# BRANCO = (255, 255, 255)
# AMARELO = (255, 223, 0)
# CINZA_ESCURO = (50, 50, 50)

# fundo = pygame.image.load("Springfield.jpg")
# fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

# botaojogar = pygame.image.load('BotaoJogar.png')
# botaojogar = pygame.transform.scale(botaojogar,(250,125))
# botaojogar_rect = botaojogar.get_rect(center=(400, 500))

# personagem = pygame.image.load("Bart.png")
# personagem_rect = personagem.get_rect(bottomright=(LARGURA-20, ALTURA))

# fonte_titulo = pygame.font.SysFont("comicsansms", 60, bold=True)
# titulo = fonte_titulo.render("Subway Simpsons", True, AMARELO)
# titulo_rect = titulo.get_rect(center=(LARGURA / 2, 25))

# fonte_botao = pygame.font.SysFont("comicsans", 40)

import pygame

# Configurações de tela
LARGURA = 800
ALTURA = 600
WIDTH, HEIGHT = 600, 800  # Para o jogo principal

# Cores
BRANCO = (255, 255, 255)
AMARELO = (255, 223, 0)
CINZA_ESCURO = (50, 50, 50)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

# Configurações do jogo principal
LANES = 3
lane_width = WIDTH // LANES
player_y = HEIGHT - 150
player_speed = 5
BASE_OBSTACLE_SPEED = 7
MAX_OBSTACLE_SPEED = 20
SPEED_INCREASE_INTERVAL = 100
BASE_OBSTACLE_SPAWN_RATE = 60
MIN_OBSTACLE_SPAWN_RATE = 30
OBSTACLE_INCREASE_SPEED = 15
COIN_SPAWN_RATE = 100

# Recursos gráficos para a tela inicial
fundo = pygame.image.load("Springfield.jpg")
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

botaojogar = pygame.image.load('BotaoJogar.png')
botaojogar = pygame.transform.scale(botaojogar, (250, 125))
botaojogar_rect = botaojogar.get_rect(center=(400, 500))

personagem = pygame.image.load("Bart.png")
personagem_rect = personagem.get_rect(bottomright=(LARGURA-20, ALTURA))

rosquinha = pygame.image.load("rosquinha.png")
rosquinha = pygame.transform.scale(rosquinha, (40, 40))

fonte_titulo = pygame.font.SysFont("comicsansms", 60, bold=True)
titulo = fonte_titulo.render("Subway Simpsons", True, AMARELO)
titulo_rect = titulo.get_rect(center=(LARGURA / 2, 25))

fonte_botao = pygame.font.SysFont("comicsans", 40)