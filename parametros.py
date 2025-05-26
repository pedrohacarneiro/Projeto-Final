import pygame

# Configurações de tela
WIDTH, HEIGHT = 500, 700  # Largura aumentada para 700
LARGURA, ALTURA = 1000, 600  # Para a tela inicial

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
VERDE_FINAL = (130,202,40)

# Variável global para armazenar o recorde
high_score = 0

# Configurações do jogo principal
LANES = 3
lane_width = WIDTH // LANES  # Cada pista terá ~233 pixels
player_y = HEIGHT - 180  # Ajustado para nova altura dos carros
player_speed = 5
odd_cerveja = 0.15
# Dimensões dos objetos
OBSTACLE_WIDTH = 100
OBSTACLE_HEIGHT = 240
PLAYER_WIDTH = 60
PLAYER_HEIGHT = 100
COIN_SIZE = 40

# Configurações de velocidade
BASE_OBSTACLE_SPEED = 10
MAX_OBSTACLE_SPEED = 20
SPEED_INCREASE_INTERVAL = 100
BASE_OBSTACLE_SPAWN_RATE = 60
MIN_OBSTACLE_SPAWN_RATE = 30
OBSTACLE_INCREASE_SPEED = 17
COIN_SPAWN_RATE = 100
FPS = 120
contador = 0

# Recursos gráficos para a tela inicial
fundo = pygame.image.load("Springfield.jpg")
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

botaojogar = pygame.image.load('BotaoJogar.png')
botaojogar = pygame.transform.scale(botaojogar, (250, 200))
botaojogar_rect = botaojogar.get_rect(center=(500, 500))

personagem = pygame.image.load("Bart.png")
personagem = pygame.transform.scale(personagem, (300, 500))
personagem_rect = personagem.get_rect(bottomright=(LARGURA-20, ALTURA))

rosquinha = pygame.image.load("rosquinha.png")
rosquinha = pygame.transform.scale(rosquinha, (COIN_SIZE, COIN_SIZE))

cerveja = pygame.image.load("Cerveja.png")
cerveja = pygame.transform.scale(cerveja, (COIN_SIZE, COIN_SIZE))
cerveja_rect = cerveja.get_rect(topright=(WIDTH - 10, 10))

fonte_titulo = pygame.font.SysFont("comicsansms", 60, bold=True)
titulo = fonte_titulo.render("Springfield Surfers", True, AMARELO)
titulo_rect = titulo.get_rect(center=(LARGURA / 2, 250))

gameoverimagem = pygame.image.load("gameoverimagem.png")
gameoverimagem = pygame.transform.scale(gameoverimagem, (400, 350))
gameoverimagem_rect = gameoverimagem.get_rect(center=(WIDTH/2, 530))

# comojogar_imagem = pygame.image.load("Imagemcomojogar.jpg")  
# comojogar_imagem = pygame.transform.scale(comojogar_imagem, (LARGURA, ALTURA))
# comojogar_rect = comojogar_imagem.get_rect()

# Caminhos das imagens dos obstáculos (carros)
IMAGENS_CARROS = [
    "carroazul.png",
    "CARROCINZA.png",
    "Carropoliciasimpsons (2).png",
    "carrotaxi.png",
    "carroverde.png",
    "carrovermelho.png"
]

# Caminhos das imagens dos fundos
IMAGENS_FUNDOS = [
    "f1.png",
    "f2.png",
    "f3.png",
    "f4.png",
    "f5.png",
    "f6.png",
    "f7.png",
    "f8.png",
    "f9.png",
    "f10.png",
    "f11.png",
    "f12.png",
    "f13.png",
    "f14.png",
    "f15.png",
    "f16.png"
]

frames = [
    pygame.transform.scale(pygame.image.load('Framebart1.png'), (PLAYER_WIDTH*1.8, PLAYER_HEIGHT*1.5)),
    pygame.transform.scale(pygame.image.load('Framebart2.png'), (PLAYER_WIDTH*1.8, PLAYER_HEIGHT*1.5)),
    pygame.transform.scale(pygame.image.load('Framebart3.png'), (PLAYER_WIDTH*1.8, PLAYER_HEIGHT*1.5)),
    pygame.transform.scale(pygame.image.load('Framebart4.png'), (PLAYER_WIDTH*1.8, PLAYER_HEIGHT*1.5)),
    pygame.transform.scale(pygame.image.load('Framebart5.png'), (PLAYER_WIDTH*1.8, PLAYER_HEIGHT*1.5)),
    pygame.transform.scale(pygame.image.load('Framebart6.png'), (PLAYER_WIDTH*1.8, PLAYER_HEIGHT*1.5)),
    pygame.transform.scale(pygame.image.load('Framebart7.png'), (PLAYER_WIDTH*1.5, PLAYER_HEIGHT*1.7)),
    pygame.transform.scale(pygame.image.load('Framebart8.png'), (PLAYER_WIDTH*1.8, PLAYER_HEIGHT*1.5)),
]

som_comendo = pygame.mixer.Sound("Somcomendo.mp3")
som_cerveja = pygame.mixer.Sound("abrindocerveja.mp3")

