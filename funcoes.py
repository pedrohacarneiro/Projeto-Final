# import pygame
# from parametros import *

# def tela_inicial(jogo, TELA,fundo,titulo_rect,personagem,personagem_rect,tela_atual):
#     TELA.blit(fundo, (0, 0))
#     TELA.blit(titulo, titulo_rect)
#     TELA.blit(personagem, personagem_rect)
#     TELA.blit(botaojogar, botaojogar_rect)
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             jogo = False

#     pygame.display.update()

#     return jogo, tela_atual

# def tela_jogo(TELA):
#     rodando = True
#     TELA.fill((255, 255, 255))
#     pygame.display.update()
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             rodando = False
#     return rodando, "tela jogo"

import pygame
import random
import sys
from parametros import *

class Player:
    def __init__(self):
        self.width = 50
        self.height = 80
        self.x = lane_width * 1 + (lane_width - self.width) // 2
        self.y = player_y
        self.lane = 1

    def draw(self, screen):
        pygame.draw.rect(screen, YELLOW, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, 20))
        pygame.draw.rect(screen, RED, (self.x, self.y + 20, self.width, 20))

    def move(self, direction):
        if direction == "left" and self.lane > 0:
            self.lane -= 1
        elif direction == "right" and self.lane < LANES - 1:
            self.lane += 1
        self.x = self.lane * lane_width + (lane_width - self.width) // 2

class Obstacle:
    def __init__(self, lane):
        self.width = 50
        self.height = 50
        self.lane = lane
        self.x = lane * lane_width + (lane_width - self.width) // 2
        self.y = -self.height

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

    def update(self, speed):
        self.y += speed
        return self.y > HEIGHT

class Coin:
    def __init__(self, lane):
        self.width = 30
        self.height = 30
        self.lane = lane
        self.x = lane * lane_width + (lane_width - self.width) // 2
        self.y = -self.height

    def draw(self, screen):
        pygame.draw.ellipse(screen, GOLD, (self.x, self.y, self.width, self.height))

    def update(self, speed):
        self.y += speed
        return self.y > HEIGHT

def is_position_free(lane, objects):
    for obj in objects:
        if obj.lane == lane:
            return False
    return True

def draw_hud(screen, meters, speed, high_score):
    font = pygame.font.SysFont(None, 36)
    
    # Contador de metros
    meter_text = font.render(f"Metros: {meters}", True, BLACK)
    text_rect = meter_text.get_rect(topleft=(10, 10))
    pygame.draw.rect(screen, YELLOW, (text_rect.x - 5, text_rect.y - 5, text_rect.width + 10, text_rect.height + 10))
    screen.blit(meter_text, (10, 10))
    
    # Contador de recorde
    high_score_text = font.render(f"Recorde: {high_score}", True, BLACK)
    high_score_rect = high_score_text.get_rect(topleft=(10, 50))
    pygame.draw.rect(screen, YELLOW, (high_score_rect.x - 5, high_score_rect.y - 5, high_score_rect.width + 10, high_score_rect.height + 10))
    screen.blit(high_score_text, (10, 50))
    
    # Contador de velocidade
    speed_text = font.render(f"Velocidade: {speed}", True, BLACK)
    speed_rect = speed_text.get_rect(topleft=(10, 90))
    pygame.draw.rect(screen, YELLOW, (speed_rect.x - 5, speed_rect.y - 5, speed_rect.width + 10, speed_rect.height + 10))
    screen.blit(speed_text, (10, 90))

def draw_button(screen, text, x, y, width, height, inactive_color, active_color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, active_color, (x, y, width, height))
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))

    font = pygame.font.SysFont(None, 40)
    text_surf = font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=(x + width/2, y + height/2))
    screen.blit(text_surf, text_rect)
    return False

def game_over_screen(screen, final_meters, high_score):
    screen.fill(BLACK)
    font_large = pygame.font.SysFont(None, 72)
    font_medium = pygame.font.SysFont(None, 48)
    
    # Texto Game Over
    game_over_text = font_large.render("GAME OVER", True, RED)
    game_over_rect = game_over_text.get_rect(center=(WIDTH/2, HEIGHT/4))
    screen.blit(game_over_text, game_over_rect)
    
    # Pontuação final
    score_text = font_medium.render(f"Metros: {final_meters}", True, WHITE)
    score_rect = score_text.get_rect(center=(WIDTH/2, HEIGHT/3))
    screen.blit(score_text, score_rect)
    
    # Recorde
    high_score_text = font_medium.render(f"Recorde: {high_score}", True, WHITE)
    high_score_rect = high_score_text.get_rect(center=(WIDTH/2, HEIGHT/2.4))
    screen.blit(high_score_text, high_score_rect)
    
    # Botão de reiniciar
    restart = False
    while not restart:
        restart = draw_button(screen, "REINICIAR", WIDTH/2 - 100, HEIGHT*2/3, 200, 50, GRAY, WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.flip()
        pygame.time.Clock().tick(60)
    
    return True

def tela_inicial(jogo, TELA, fundo, titulo_rect, personagem, personagem_rect, tela_atual):
    TELA.blit(fundo, (0, 0))
    TELA.blit(titulo, titulo_rect)
    TELA.blit(personagem, personagem_rect)
    TELA.blit(botaojogar, botaojogar_rect)
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if botaojogar_rect.collidepoint(mouse) and click[0] == 1:
        tela_atual = "tela jogo"
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo = False

    pygame.display.update()
    return jogo, tela_atual

def tela_jogo(TELA):
    # Configurações específicas do jogo
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    high_score = 0
    
    player = Player()
    obstacles = []
    coins = []
    meters = 0
    current_obstacle_speed = BASE_OBSTACLE_SPEED
    speed_increase_threshold = SPEED_INCREASE_INTERVAL
    obstacle_timer = 0
    coin_timer = 0
    meter_timer = 0

    running = True
    while running:
        screen.fill(BLACK)

        # Aumento progressivo de velocidade
        if meters >= speed_increase_threshold:
            current_obstacle_speed = min(BASE_OBSTACLE_SPEED + (meters // SPEED_INCREASE_INTERVAL), MAX_OBSTACLE_SPEED)
            speed_increase_threshold += SPEED_INCREASE_INTERVAL

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False, "tela inicial"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move("left")
                elif event.key == pygame.K_RIGHT:
                    player.move("right")

        # Geração de obstáculos
        obstacle_timer += 1
        spawn_rate = BASE_OBSTACLE_SPAWN_RATE

        if current_obstacle_speed >= OBSTACLE_INCREASE_SPEED:
            reduction = (current_obstacle_speed - OBSTACLE_INCREASE_SPEED) * 3
            spawn_rate = max(BASE_OBSTACLE_SPAWN_RATE - reduction, MIN_OBSTACLE_SPAWN_RATE)

        if obstacle_timer >= spawn_rate:
            if current_obstacle_speed >= OBSTACLE_INCREASE_SPEED and random.random() < 0.4:
                lanes = random.sample(range(LANES), min(2, LANES))
                for lane in lanes:
                    obstacles.append(Obstacle(lane))
            else:
                obstacles.append(Obstacle(random.randint(0, LANES - 1)))
            obstacle_timer = 0

        # Geração de moedas
        coin_timer += 1
        if coin_timer >= COIN_SPAWN_RATE:
            free_lanes = [lane for lane in range(LANES) if is_position_free(lane, obstacles)]
            if free_lanes:
                coins.append(Coin(random.choice(free_lanes)))
                coin_timer = 0

        # Atualização dos obstáculos
        for obstacle in obstacles[:]:
            if obstacle.update(current_obstacle_speed):
                obstacles.remove(obstacle)
            obstacle.draw(screen)

        # Atualização das moedas
        for coin in coins[:]:
            if coin.update(current_obstacle_speed):
                coins.remove(coin)
            coin.draw(screen)

            # Colisão com moedas
            if (player.x < coin.x + coin.width and
                player.x + player.width > coin.x and
                player.y < coin.y + coin.height and
                player.y + player.height > coin.y):
                coins.remove(coin)
                meters += 10

        # Atualização dos metros
        meter_timer += 1
        if meter_timer >= 60:
            meters += 1
            meter_timer = 0

        # Colisão com obstáculos
        for obstacle in obstacles:
            if (player.x < obstacle.x + obstacle.width and
                player.x + player.width > obstacle.x and
                player.y < obstacle.y + obstacle.height and
                player.y + player.height > obstacle.y):
                running = False

        # Desenho do jogador e HUD
        player.draw(screen)
        draw_hud(screen, meters, current_obstacle_speed, high_score)

        pygame.display.flip()
        clock.tick(60)

    # Ao sair do loop do jogo, mostra a tela de Game Over
    if game_over_screen(screen, meters, high_score):
        return True, "tela jogo"  # Reinicia o jogo
    else:
        return True, "tela inicial"  # Volta para tela inicial