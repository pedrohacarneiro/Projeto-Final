import pygame
import random
import sys
from parametros import *


class Player:
    def __init__(self):
        self.width = PLAYER_WIDTH * 2  # Dobrando o tamanho original
        self.height = PLAYER_HEIGHT * 2  # Dobrando o tamanho original
        self.lane = 1
        self.x = (lane_width * self.lane) + (lane_width - self.width) // 2
        self.target_x = self.x  # Posição alvo para o deslizamento
        self.y = player_y
        self.frames = frames
        self.current_frame = 0
        self.animation_timer = 0
        self.animation_speed = 0.13  # segundos por frame
        self.slide_speed = 15  # Velocidade do deslizamento
        # Área de colisão ainda menor que o sprite
        self.collision_width = self.width * 0.5  # 50% da largura
        self.collision_height = self.height * 0.5  # 50% da altura

    def get_collision_rect(self):
        # Retorna um retângulo de colisão centralizado no sprite
        x = self.x + (self.width - self.collision_width) // 2
        y = self.y + (self.height - self.collision_height) // 2
        return pygame.Rect(x, y, self.collision_width, self.collision_height)

    def update_animation(self, dt):
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)

    def update_position(self):
        # Atualiza a posição x para criar o efeito de deslizamento
        if self.x < self.target_x:
            self.x = min(self.x + self.slide_speed, self.target_x)
        elif self.x > self.target_x:
            self.x = max(self.x - self.slide_speed, self.target_x)

    def draw(self, screen):
        # Desenha o sprite na posição x com o tamanho original
        screen.blit(self.frames[self.current_frame], (self.x, self.y))
        
        # Desenha os retângulos coloridos apenas quando intangível
        if hasattr(self, 'intangibility') and self.intangibility:
            pygame.draw.rect(screen, (0, 255, 255), (self.x, self.y, self.width, self.height), 4)

    def move(self, direction):
        if direction == "left" and self.lane > 0:
            self.lane -= 1
            self.target_x = (lane_width * self.lane) + (lane_width - self.width) // 2
        elif direction == "right" and self.lane < LANES - 1:
            self.lane += 1
            self.target_x = (lane_width * self.lane) + (lane_width - self.width) // 2

class Obstacle:
    def __init__(self, lane):
        self.lane = lane
        self.image = carregar_imagem_obstaculo()
        
        # Calcula dimensões mantendo proporção
        img_width, img_height = self.image.get_size()
        aspect_ratio = img_width / img_height
        
        # Define altura fixa e calcula largura proporcional
        self.height = OBSTACLE_HEIGHT
        self.width = int(self.height * aspect_ratio)
        
        # Ajusta se for muito largo
        if self.width > lane_width - 20:
            self.width = lane_width - 20
            self.height = int(self.width / aspect_ratio)
        
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.x = lane * lane_width + (lane_width - self.width) // 2
        self.y = -self.height

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self, speed):
        self.y += speed
        return self.y > HEIGHT

class Coin:
    def __init__(self, lane):
        self.width = COIN_SIZE
        self.height = COIN_SIZE
        self.lane = lane
        self.x = lane * lane_width + (lane_width - self.width) // 2
        self.y = -self.height

    def draw(self, screen, coin_img):
        screen.blit(coin_img, (self.x, self.y))

    def update(self, speed):
        self.y += speed
        return self.y > HEIGHT

class SuperPower:
    def __init__(self, lane):
        self.width = COIN_SIZE 
        self.height = COIN_SIZE
        self.lane = lane
        self.x = lane * lane_width + (lane_width - self.width) // 2
        self.y = -self.height

    def draw(self, screen, cerveja_img):
        screen.blit(cerveja_img, (self.x, self.y))

    def update(self, speed):
        self.y += speed
        return self.y > HEIGHT

class BackgroundManager:
    def __init__(self):
        self.images = [pygame.image.load(img).convert_alpha() for img in IMAGENS_FUNDOS]
        self.current_bg_index = random.randint(0, len(self.images) - 1)
        self.next_bg_index = self.get_next_random_index(self.current_bg_index)
        self.current_bg = pygame.transform.scale(self.images[self.current_bg_index], (WIDTH, HEIGHT))
        self.next_bg = pygame.transform.scale(self.images[self.next_bg_index], (WIDTH, HEIGHT))
        self.current_y = 0
        self.next_y = -HEIGHT
        self.speed = 5

    
        
    def get_next_random_index(self, current_index):
        next_index = random.randint(0, len(self.images) - 1)
        while next_index == current_index and len(self.images) > 1:
            next_index = random.randint(0, len(self.images) - 1)
        return next_index
        
    def update(self):
        self.current_y += self.speed
        self.next_y += self.speed

        # Quando o fundo atual sair completamente da tela:
        if self.current_y >= HEIGHT:
            # Reposiciona o atual para ocupar o lugar do próximo
            self.current_bg = self.next_bg
            self.current_bg_index = self.next_bg_index
            self.current_y = self.next_y

            # Define o novo próximo fundo, acima da tela
            self.next_bg_index = self.get_next_random_index(self.current_bg_index)
            self.next_bg = pygame.transform.scale(self.images[self.next_bg_index], (int(WIDTH), int(HEIGHT)))
            self.next_y = self.current_y - HEIGHT  # Agora sim, novo fundo acima
            
    def draw(self, screen):
        screen.blit(self.current_bg, (0, int(self.current_y)))
        screen.blit(self.next_bg, (0, int(self.next_y)))


def is_position_free(lane, objects):
    for obj in objects:
        if obj.lane == lane and obj.y > -obj.height:
            return False
    return True

def draw_hud(screen, meters, speed, high_score):
    font = pygame.font.SysFont(None, 36)
    
    meter_text = font.render(f"Pontuação: {meters}", True, BLACK)
    text_rect = meter_text.get_rect(topleft=(10, 10))
    pygame.draw.rect(screen, YELLOW, (text_rect.x - 5, text_rect.y - 5, text_rect.width + 10, text_rect.height + 10))
    screen.blit(meter_text, (10, 10))
    
    speed_text = font.render(f"Velocidade: {speed}", True, BLACK)
    speed_rect = speed_text.get_rect(topleft=(10, 50))
    pygame.draw.rect(screen, YELLOW, (speed_rect.x - 5, speed_rect.y - 5, speed_rect.width + 10, speed_rect.height + 10))
    screen.blit(speed_text, (10, 50))
    
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
    screen.fill(VERDE_FINAL)

    screen.blit(gameoverimagem, gameoverimagem_rect)

    font_large = pygame.font.SysFont(None, 72)
    font_medium = pygame.font.SysFont(None, 48)
    
    game_over_text = font_large.render("GAME OVER", True, BLACK)
    game_over_rect = game_over_text.get_rect(center=(WIDTH/2, HEIGHT/8))
    screen.blit(game_over_text, game_over_rect)
    
    score_text = font_medium.render(f"Pontuação atual: {final_meters}", True, WHITE)
    score_rect = score_text.get_rect(center=(WIDTH/2, HEIGHT/5))
    screen.blit(score_text, score_rect)
    
    high_score_text = font_medium.render(f"Recorde: {high_score}", True, WHITE)
    high_score_rect = high_score_text.get_rect(center=(WIDTH/2, HEIGHT/4))
    screen.blit(high_score_text, high_score_rect)
    
    restart = False
    while not restart:
        restart = draw_button(screen, "REINICIAR", WIDTH/2 - 100, HEIGHT*2/6, 200, 50, GOLD, WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.flip()
        pygame.time.Clock().tick(60)
    
    return True

def tela_inicial(jogo, TELA, fundo, titulo, titulo_rect, personagem, personagem_rect, botaojogar, botaojogar_rect, tela_atual, contador):
    TELA.blit(fundo, (0, 0))
    TELA.blit(titulo, titulo_rect)
    TELA.blit(personagem, personagem_rect)
    TELA.blit(botaojogar, botaojogar_rect)

    if contador == 0:
        pygame.mixer.music.load("inicio.mp3")
        pygame.mixer.music.play(loops=1)
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    contador += 1
    if botaojogar_rect.collidepoint(mouse) and click[0] == 1:
        tela_atual = "tela jogo"
        contador = 0
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo = False

    pygame.display.update()
    return jogo, tela_atual, contador

def tela_jogo(TELA, contador):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    
    global high_score
    
    player = Player()
    obstacles = []
    coins = []
    meters = 0
    current_obstacle_speed = BASE_OBSTACLE_SPEED
    speed_increase_threshold = SPEED_INCREASE_INTERVAL
    obstacle_timer = 0
    coin_timer = 0
    meter_timer = 0
    
    super_powers = []
    power_timer = 0
    power_cooldown = 0  # New variable for power spawn cooldown
    intangibility = False
    intangibility_end_time = 0

    bg_manager = BackgroundManager()
    
    if contador == 0:
        pygame.mixer.music.load("trilha.mp3")
        pygame.mixer.music.play(loops=-1)  # Loop infinito
    
    contador += 1
    
    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0  # Delta time em segundos
        
        player.update_animation(dt)
        player.update_position()  # Atualiza a posição do jogador
        
        screen.fill((0, 0, 0))  # Limpa a tela

        
        # Atualiza e desenha o fundo
        bg_manager.speed = current_obstacle_speed * 0.5
        bg_manager.update()
        bg_manager.draw(screen)
        
        if meters > high_score:
            high_score = meters

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

        obstacle_timer += 1
        spawn_rate = max(BASE_OBSTACLE_SPAWN_RATE - (meters // 50), MIN_OBSTACLE_SPAWN_RATE)

        if obstacle_timer >= spawn_rate:
            if current_obstacle_speed >= OBSTACLE_INCREASE_SPEED and random.random() < 0.3:
                lanes = random.sample(range(LANES), min(2, LANES))
                for lane in lanes:
                    if is_position_free(lane, obstacles):
                        obstacles.append(Obstacle(lane))
            else:
                lane = random.randint(0, LANES - 1)
                if is_position_free(lane, obstacles):
                    obstacles.append(Obstacle(lane))
            obstacle_timer = 0

        coin_timer += 1
        if coin_timer >= COIN_SPAWN_RATE:
            free_lanes = []

            for lane in range(LANES):
                lane_is_clear = True
                # Check for obstacles
                for obs in obstacles:
                    if obs.lane == lane and obs.y < COIN_SIZE * 2:
                        lane_is_clear = False
                        break
                # Check for coins
                for coin in coins:
                    if coin.lane == lane and coin.y < COIN_SIZE * 2:
                        lane_is_clear = False
                        break
                # Check for powers
                for power in super_powers:
                    if power.lane == lane and power.y < COIN_SIZE * 2:
                        lane_is_clear = False
                        break
                if lane_is_clear:
                    free_lanes.append(lane)

            if free_lanes:
                coins.append(Coin(random.choice(free_lanes)))
                coin_timer = 0

            # Spawn power in a different lane than coins
            if random.random() < odd_cerveja and free_lanes and power_cooldown <= 0:
                # Remove lanes that have coins
                power_free_lanes = [lane for lane in free_lanes if not any(coin.lane == lane for coin in coins)]
                if power_free_lanes:
                    super_powers.append(SuperPower(random.choice(power_free_lanes)))
                    power_cooldown = 1200  # 20 seconds * 60 FPS = 1200 frames

        # Update power cooldown
        if power_cooldown > 0:
            power_cooldown -= 1

        for obstacle in obstacles[:]:
            if obstacle.update(current_obstacle_speed):
                obstacles.remove(obstacle)
            else:
                obstacle.draw(screen)

        for coin in coins[:]:
            if coin.update(current_obstacle_speed):
                coins.remove(coin)
            else:
                coin.draw(screen, rosquinha)

                if (player.x < coin.x + coin.width and
                    player.x + player.width > coin.x and
                    player.y < coin.y + coin.height and
                    player.y + player.height > coin.y):
                    som_comendo.play()
                    coins.remove(coin)
                    meters += 10

        for power in super_powers[:]:
            if power.update(current_obstacle_speed):
                super_powers.remove(power)
            else:
                power.draw(screen, cerveja)  

                if (player.x < power.x + power.width and
                    player.x + player.width > power.x and
                    player.y < power.y + power.height and
                    player.y + player.height > power.y):
                    som_cerveja.play()
                    super_powers.remove(power)
                    intangibility = True
                    intangibility_timer = 180
        if intangibility:
            intangibility_timer -= 1
            if intangibility_timer <= 0:
                intangibility = False

        meter_timer += 1
        if meter_timer >= 60:
            meters += 1
            meter_timer = 0
        if not intangibility:
            for obstacle in obstacles:
                player_rect = player.get_collision_rect()
                obstacle_rect = pygame.Rect(obstacle.x, obstacle.y, obstacle.width, obstacle.height)
                
                if player_rect.colliderect(obstacle_rect):
                    running = False
                    contador = 0

        player.draw(screen)
        if intangibility:
            pygame.draw.rect(screen, (0, 255, 255), (player.x, player.y, player.width, player.height), 4)
        draw_hud(screen, meters, current_obstacle_speed, high_score)

        pygame.display.flip()
        clock.tick(FPS)

    if game_over_screen(screen, meters, high_score):
        return True, "tela jogo", contador
    else:
        return True, "tela inicial", contador
    
def carregar_imagem_obstaculo():
    try:
        caminho_imagem = random.choice(IMAGENS_CARROS)
        imagem = pygame.image.load(caminho_imagem).convert_alpha()
        return imagem
    except Exception as e:
        print(f"Erro ao carregar imagem: {e}")
        surf = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(surf, RED, (0, 0, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        return surf
