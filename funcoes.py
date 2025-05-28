import pygame
import random
import sys
from parametros import *


class Player:
    """
    Classe que representa o jogador (Bart Simpson) no jogo.
    
    Attributes:
        width (int): Largura do sprite do jogador
        height (int): Altura do sprite do jogador
        lane (int): Faixa atual do jogador (0-2)
        x (int): Posição horizontal atual
        target_x (int): Posição horizontal alvo para movimento suave
        y (int): Posição vertical fixa
        frames (list): Lista de frames da animação
        current_frame (int): Frame atual da animação
        animation_timer (float): Timer para controle da animação
        animation_speed (float): Velocidade da animação em segundos por frame
        slide_speed (int): Velocidade do deslizamento lateral
        collision_width (float): Largura da área de colisão
        collision_height (float): Altura da área de colisão
    """
    def __init__(self):
        self.width = PLAYER_WIDTH * 2  
        self.height = PLAYER_HEIGHT * 2 
        self.lane = 1
        self.x = (lane_width * self.lane) + (lane_width - self.width) // 2
        self.target_x = self.x  
        self.y = player_y
        self.frames = frames
        self.current_frame = 0
        self.animation_timer = 0
        self.animation_speed = 0.13  
        self.slide_speed = 15  
        self.collision_width = self.width * 0.5  
        self.collision_height = self.height * 0.5  

    def get_collision_rect(self):
        """
        Retorna o retângulo de colisão centralizado no sprite do jogador.
        
        Returns:
            pygame.Rect: Retângulo de colisão centralizado
        """
        x = self.x + (self.width - self.collision_width) // 2
        y = self.y + (self.height - self.collision_height) // 2
        return pygame.Rect(x, y, self.collision_width, self.collision_height)

    def update_animation(self, dt):
        """
        Atualiza a animação do jogador baseado no tempo delta.
        
        Args:
            dt (float): Tempo delta em segundos desde o último frame
        """
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)

    def update_position(self):
        """
        Atualiza a posição horizontal do jogador para criar movimento suave.
        Move o jogador em direção à posição alvo (target_x).
        """
        if self.x < self.target_x:
            self.x = min(self.x + self.slide_speed, self.target_x)
        elif self.x > self.target_x:
            self.x = max(self.x - self.slide_speed, self.target_x)

    def draw(self, screen):
        """
        Desenha o sprite do jogador na tela.
        
        Args:
            screen (pygame.Surface): Superfície onde o jogador será desenhado
        """
        screen.blit(self.frames[self.current_frame], (self.x, self.y))


    def move(self, direction):
        """
        Move o jogador para a esquerda ou direita.
        
        Args:
            direction (str): Direção do movimento ("left" ou "right")
        """
        if direction == "left" and self.lane > 0:
            self.lane -= 1
            self.target_x = (lane_width * self.lane) + (lane_width - self.width) // 2
        elif direction == "right" and self.lane < LANES - 1:
            self.lane += 1
            self.target_x = (lane_width * self.lane) + (lane_width - self.width) // 2

class Obstacle:
    """
    Classe que representa os obstáculos (carros) no jogo.
    
    Attributes:
        lane (int): Faixa onde o obstáculo está
        image (pygame.Surface): Imagem do obstáculo
        width (int): Largura do obstáculo
        height (int): Altura do obstáculo
        x (int): Posição horizontal
        y (int): Posição vertical
    """
    def __init__(self, lane):
        self.lane = lane
        self.image = carregar_imagem_obstaculo()
        
        img_width, img_height = self.image.get_size()
        aspect_ratio = img_width / img_height
        
        self.height = OBSTACLE_HEIGHT
        self.width = int(self.height * aspect_ratio)
        
        if self.width > lane_width - 20:
            self.width = lane_width - 20
            self.height = int(self.width / aspect_ratio)
        
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.x = lane * lane_width + (lane_width - self.width) // 2
        self.y = -self.height

    def draw(self, screen):
        """
        Desenha o obstáculo na tela.
        
        Args:
            screen (pygame.Surface): Superfície onde o obstáculo será desenhado
        """
        screen.blit(self.image, (self.x, self.y))

    def update(self, speed):
        """
        Atualiza a posição do obstáculo.
        
        Args:
            speed (int): Velocidade de movimento do obstáculo
            
        Returns:
            bool: True se o obstáculo saiu da tela, False caso contrário
        """
        self.y += speed
        return self.y > HEIGHT

class Coin:
    """
    Classe que representa as moedas (rosquinhas) coletáveis no jogo.
    
    Attributes:
        width (int): Largura da moeda
        height (int): Altura da moeda
        lane (int): Faixa onde a moeda está
        x (int): Posição horizontal
        y (int): Posição vertical
    """
    def __init__(self, lane):
        self.width = COIN_SIZE
        self.height = COIN_SIZE
        self.lane = lane
        self.x = lane * lane_width + (lane_width - self.width) // 2
        self.y = -self.height

    def draw(self, screen, coin_img):
        """
        Desenha a moeda na tela.
        
        Args:
            screen (pygame.Surface): Superfície onde a moeda será desenhada
            coin_img (pygame.Surface): Imagem da moeda
        """
        screen.blit(coin_img, (self.x, self.y))

    def update(self, speed):
        """
        Atualiza a posição da moeda.
        
        Args:
            speed (int): Velocidade de movimento da moeda
            
        Returns:
            bool: True se a moeda saiu da tela, False caso contrário
        """
        self.y += speed
        return self.y > HEIGHT

class SuperPower:
    """
    Classe que representa os power-ups (cervejas) no jogo.
    
    Attributes:
        width (int): Largura do power-up
        height (int): Altura do power-up
        lane (int): Faixa onde o power-up está
        x (int): Posição horizontal
        y (int): Posição vertical
    """
    def __init__(self, lane):
        self.width = COIN_SIZE 
        self.height = COIN_SIZE
        self.lane = lane
        self.x = lane * lane_width + (lane_width - self.width) // 2
        self.y = -self.height

    def draw(self, screen, cerveja_img):
        """
        Desenha o power-up na tela.
        
        Args:
            screen (pygame.Surface): Superfície onde o power-up será desenhado
            cerveja_img (pygame.Surface): Imagem do power-up
        """
        screen.blit(cerveja_img, (self.x, self.y))

    def update(self, speed):
        """
        Atualiza a posição do power-up.
        
        Args:
            speed (int): Velocidade de movimento do power-up
            
        Returns:
            bool: True se o power-up saiu da tela, False caso contrário
        """
        self.y += speed
        return self.y > HEIGHT


class BackgroundManager:
    """
    Classe que gerencia o fundo dinâmico do jogo.
    
    Attributes:
        images (list): Lista de imagens de fundo
        current_bg_index (int): Índice do fundo atual
        next_bg_index (int): Índice do próximo fundo
        current_bg (pygame.Surface): Imagem do fundo atual
        next_bg (pygame.Surface): Imagem do próximo fundo
        current_y (int): Posição vertical do fundo atual
        next_y (int): Posição vertical do próximo fundo
        speed (int): Velocidade de rolagem do fundo
    """
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
        """
        Retorna um índice aleatório diferente do atual para o próximo fundo.
        
        Args:
            current_index (int): Índice do fundo atual
            
        Returns:
            int: Índice do próximo fundo
        """
        next_index = random.randint(0, len(self.images) - 1)
        while next_index == current_index and len(self.images) > 1:
            next_index = random.randint(0, len(self.images) - 1)
        return next_index
        
    def update(self):
        """
        Atualiza as posições dos fundos e gerencia a transição entre eles.
        """
        self.current_y += self.speed
        self.next_y += self.speed

        if self.current_y >= HEIGHT:
            self.current_bg = self.next_bg
            self.current_bg_index = self.next_bg_index
            self.current_y = self.next_y

            self.next_bg_index = self.get_next_random_index(self.current_bg_index)
            self.next_bg = pygame.transform.scale(self.images[self.next_bg_index], (int(WIDTH), int(HEIGHT)))
            self.next_y = self.current_y - HEIGHT 
            
    def draw(self, screen):
        """
        Desenha os fundos na tela.
        
        Args:
            screen (pygame.Surface): Superfície onde os fundos serão desenhados
        """
        screen.blit(self.current_bg, (0, int(self.current_y)))
        screen.blit(self.next_bg, (0, int(self.next_y)))


def is_position_free(lane, objects):
    """
    Verifica se uma faixa está livre para spawn de objetos.
    
    Args:
        lane (int): Faixa a ser verificada
        objects (list): Lista de objetos para verificar colisão
        
    Returns:
        bool: True se a faixa está livre, False caso contrário
    """
    for obj in objects:
        if obj.lane == lane and obj.y > -obj.height:
            return False
    return True

def draw_hud(screen, meters, speed, high_score):
    """
    Desenha o HUD (Heads-Up Display) na tela.
    
    Args:
        screen (pygame.Surface): Superfície onde o HUD será desenhado
        meters (int): Pontuação atual
        speed (int): Velocidade atual
        high_score (int): Recorde atual
    """
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
    """
    Desenha um botão interativo na tela.
    
    Args:
        screen (pygame.Surface): Superfície onde o botão será desenhado
        text (str): Texto do botão
        x (int): Posição horizontal
        y (int): Posição vertical
        width (int): Largura do botão
        height (int): Altura do botão
        inactive_color (tuple): Cor do botão quando não selecionado
        active_color (tuple): Cor do botão quando selecionado
        
    Returns:
        bool: True se o botão foi clicado, False caso contrário
    """
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
    """
    Exibe a tela de Game Over.
    
    Args:
        screen (pygame.Surface): Superfície onde a tela será desenhada
        final_meters (int): Pontuação final
        high_score (int): Recorde atual
        
    Returns:
        bool: True se o jogador quer reiniciar, False caso contrário
    """
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
    """
    Gerencia a tela inicial do jogo.
    
    Args:
        jogo (bool): Estado do jogo
        TELA (pygame.Surface): Superfície da tela
        fundo (pygame.Surface): Imagem de fundo
        titulo (pygame.Surface): Imagem do título
        titulo_rect (pygame.Rect): Retângulo do título
        personagem (pygame.Surface): Imagem do personagem
        personagem_rect (pygame.Rect): Retângulo do personagem
        botaojogar (pygame.Surface): Imagem do botão jogar
        botaojogar_rect (pygame.Rect): Retângulo do botão jogar
        tela_atual (str): Nome da tela atual
        contador (int): Contador para controle de música
        
    Returns:
        tuple: (jogo, tela_atual, contador)
    """
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
        tela_atual = "como jogar"
        contador = 0
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo = False

    pygame.display.update()
    return jogo, tela_atual, contador

def tela_jogo(TELA, contador):
    """
    Gerencia a tela principal do jogo.
    
    Args:
        TELA (pygame.Surface): Superfície da tela
        contador (int): Contador para controle de música
        
    Returns:
        tuple: (jogo, tela_atual, contador)
    """
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
    power_cooldown = 0  
    intangibility = False
    intangibility_end_time = 0

    bg_manager = BackgroundManager()
    
    if contador == 0:
        pygame.mixer.music.load("trilha.mp3")
        pygame.mixer.music.play(loops=-1)  
    contador += 1
    
    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0  
        
        player.update_animation(dt)
        player.update_position()  
        screen.fill((0, 0, 0)) 

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
                for obs in obstacles:
                    if obs.lane == lane and obs.y < COIN_SIZE * 2:
                        lane_is_clear = False
                        break
                for coin in coins:
                    if coin.lane == lane and coin.y < COIN_SIZE * 2:
                        lane_is_clear = False
                        break
                for power in super_powers:
                    if power.lane == lane and power.y < COIN_SIZE * 2:
                        lane_is_clear = False
                        break
                if lane_is_clear:
                    free_lanes.append(lane)

            if free_lanes:
                coins.append(Coin(random.choice(free_lanes)))
                coin_timer = 0

            if random.random() < odd_cerveja and free_lanes and power_cooldown <= 0:
                power_free_lanes = [lane for lane in free_lanes if not any(coin.lane == lane for coin in coins)]
                if power_free_lanes:
                    super_powers.append(SuperPower(random.choice(power_free_lanes)))
                    power_cooldown = 1200  
        
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
                    intangibility_timer = 360
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
            screen.blit(cerveja, cerveja_rect)
            

        draw_hud(screen, meters, current_obstacle_speed, high_score)

        pygame.display.flip()
        clock.tick(FPS)

    if game_over_screen(screen, meters, high_score):
        return True, "tela jogo", contador
    else:
        return True, "tela inicial", contador
    
def carregar_imagem_obstaculo():
    """
    Carrega uma imagem aleatória para o obstáculo.
    
    Returns:
        pygame.Surface: Imagem do obstáculo ou uma superfície vermelha em caso de erro
    """
    try:
        caminho_imagem = random.choice(IMAGENS_CARROS)
        imagem = pygame.image.load(caminho_imagem).convert_alpha()
        return imagem
    except Exception as e:
        print(f"Erro ao carregar imagem: {e}")
        surf = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(surf, RED, (0, 0, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        return surf

def tela_comojogar(jogo, tela, imagem_comojogar, imagem_rect):
    """
    Gerencia a tela de instruções do jogo.
    
    Args:
        jogo (bool): Estado do jogo
        tela (pygame.Surface): Superfície da tela
        imagem_comojogar (pygame.Surface): Imagem com instruções
        imagem_rect (pygame.Rect): Retângulo da imagem
        
    Returns:
        tuple: (jogo, tela_atual)
    """
    tela.blit(imagem_comojogar, imagem_rect)
    pygame.display.update()
    
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo = False
                esperando = False
                return jogo, "tela inicial"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    esperando = False
                    return jogo, "tela jogo"
    
    return jogo, "tela inicial"