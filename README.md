# Springfield Surfers 🛹

Um jogo de corrida inspirado em Springfield, onde você controla o Bart Simpson deslizando pelas ruas da cidade, desviando de carros, coletando rosquinhas e cervejas!

## 🎮 Como Jogar

### Controles
- **Seta Esquerda**: Move o personagem para a esquerda
- **Seta Direita**: Move o personagem para a direita
- **Espaço**: Inicia o jogo (na tela "Como Jogar")

### Objetivos
- Desvie dos carros que vêm em sua direção
- Colete rosquinhas para aumentar sua pontuação
- Colete cervejas para ganhar invencibilidade temporária

## 🎯 Mecânicas do Jogo

### Sistema de Pontuação
- Cada rosquinha coletada: +10 pontos
- Pontuação base aumenta automaticamente com o tempo
- Recorde é salvo durante a sessão do jogo

### Power-ups
- **Cerveja**: Concede invencibilidade temporária (6 segundos)
- A cerveja tem um tempo de recarga de 20 segundos entre aparições
- Durante a invencibilidade, você pode passar através dos carros sem perder

### Dificuldade Progressiva
- A velocidade dos carros aumenta gradualmente
- A frequência de spawn dos obstáculos aumenta com o tempo
- Em velocidades mais altas, podem aparecer múltiplos carros simultaneamente

## 🎨 Elementos Visuais

### Personagens e Objetos
- Bart Simpson como personagem principal
- Diversos carros como obstáculos
- Rosquinhas como itens de coleta
- Cervejas como power-ups

### Cenários
- Fundos dinâmicos que mudam automaticamente
- 16 diferentes cenários de Springfield
- Transição suave entre os cenários

## 🎵 Áudio
- Trilha sonora durante o jogo
- Efeitos sonoros para:
  - Coleta de rosquinhas
  - Coleta de cervejas
  - Música de fundo temática

## 💻 Requisitos Técnicos

### Dependências
- Python 3.x
- Pygame

### Arquivos Necessários
- Todas as imagens dos carros
- Imagens de fundo
- Sprites do Bart
- Arquivos de áudio
- Imagens da interface

## 🏆 Sistema de Recordes
- O jogo mantém registro da maior pontuação durante a sessão
- A pontuação é exibida durante o jogo e na tela de Game Over

## 🎯 Dicas
- Mantenha-se no centro da pista para ter mais tempo de reação
- Use a invencibilidade da cerveja estrategicamente
- Priorize coletar rosquinhas quando possível
- Fique atento aos padrões de movimento dos carros

## 🛠️ Desenvolvimento
O jogo foi desenvolvido usando:
- Python como linguagem principal
- Pygame para gráficos e áudio
- Sistema de colisão personalizado
- Gerenciamento de estados para diferentes telas

## 📝 Notas
- O jogo salva o recorde apenas durante a sessão atual
- A dificuldade aumenta progressivamente para manter o desafio
- O sistema de spawn de itens foi balanceado para manter o jogo divertido e desafiador

## 👥 Integrantes do Grupo

- Lucas Martins Cavalcante
- Pedro Henrique Abrahão Carneiro
- Rafael Villela Semenovich

---

## ▶️ Como Rodar o Jogo

1. Instale o Python: https://www.python.org/downloads/
2. Instale o Pygame:
   pip install pygame
3. Execute o jogo:
   python jogo.py

---

## 🎬 Vídeo de Demonstração

Assista a uma demonstração rápida do jogo funcionando:  
👉 [LINK DO VÍDEO AQUI]


---

## 🎮 Controles

- **Seta Esquerda (<)**: mover para a esquerda  
- **Seta Direita (>)**: mover para a direita  
- **Rosquinhas 🍩**: aumentam a pontuação  
- **Cervejas 🍺**: tornam o jogador imortal por 6 segundos

## 📚 Documentação das Funções

### Classes

#### Player
```python
class Player:
```
Classe que gerencia o personagem principal (Bart Simpson).

**Atributos:**
- `width`, `height`: Dimensões do personagem
- `lane`: Pista atual (0-2)
- `x`, `y`: Posição atual
- `target_x`: Posição alvo para movimento suave
- `frames`: Lista de sprites para animação
- `current_frame`: Frame atual da animação
- `animation_timer`: Timer para controle de animação
- `slide_speed`: Velocidade de deslizamento
- `collision_width`, `collision_height`: Dimensões da área de colisão

**Métodos:**
- `get_collision_rect()`: Retorna retângulo de colisão
- `update_animation(dt)`: Atualiza a animação do personagem
- `update_position()`: Atualiza a posição com movimento suave
- `draw(screen)`: Desenha o personagem na tela
- `move(direction)`: Move o personagem entre pistas

#### BackgroundManager
```python
class BackgroundManager:
```
Gerencia o sistema de fundos dinâmicos do jogo.

**Atributos:**
- `images`: Lista de imagens de fundo
- `current_bg_index`, `next_bg_index`: Índices dos fundos atual e próximo
- `current_bg`, `next_bg`: Superfícies dos fundos atual e próximo
- `current_y`, `next_y`: Posições Y dos fundos
- `speed`: Velocidade de rolagem

**Métodos:**
- `get_next_random_index(current_index)`: Seleciona próximo fundo aleatório
- `update()`: Atualiza posições dos fundos
- `draw(screen)`: Desenha os fundos na tela

### Funções de Utilidade

#### is_position_free
```python
def is_position_free(lane, objects):
```
Verifica se uma pista está livre para spawn de objetos.

**Parâmetros:**
- `lane`: Número da pista (0-2)
- `objects`: Lista de objetos a verificar

**Retorno:**
- `bool`: True se a pista estiver livre

#### draw_hud
```python
def draw_hud(screen, meters, speed, high_score):
```
Desenha o HUD (Heads-Up Display) do jogo.

**Parâmetros:**
- `screen`: Superfície do Pygame
- `meters`: Pontuação atual
- `speed`: Velocidade atual
- `high_score`: Recorde atual

#### draw_button
```python
def draw_button(screen, text, x, y, width, height, inactive_color, active_color):
```
Desenha um botão interativo na tela.

**Parâmetros:**
- `screen`: Superfície do Pygame
- `text`: Texto do botão
- `x`, `y`: Posição do botão
- `width`, `height`: Dimensões do botão
- `inactive_color`: Cor quando não selecionado
- `active_color`: Cor quando selecionado

**Retorno:**
- `bool`: True se o botão foi clicado

### Funções de Tela

#### tela_inicial
```python
def tela_inicial(jogo, TELA, fundo, titulo, titulo_rect, personagem, personagem_rect, botaojogar, botaojogar_rect, tela_atual, contador):
```
Gerencia a tela inicial do jogo.

**Parâmetros:**
- `jogo`: Estado do jogo
- `TELA`: Superfície do Pygame
- `fundo`: Imagem de fundo
- `titulo`, `titulo_rect`: Texto e retângulo do título
- `personagem`, `personagem_rect`: Sprite e retângulo do personagem
- `botaojogar`, `botaojogar_rect`: Sprite e retângulo do botão
- `tela_atual`: Estado atual da tela
- `contador`: Contador para controle de música

**Retorno:**
- Tupla com estado do jogo, próxima tela e contador

#### tela_jogo
```python
def tela_jogo(TELA, contador):
```
Gerencia a tela principal do jogo.

**Parâmetros:**
- `TELA`: Superfície do Pygame
- `contador`: Contador para controle de música

**Retorno:**
- Tupla com estado do jogo, próxima tela e contador

#### tela_comojogar
```python
def tela_comojogar(jogo, tela, imagem_comojogar, imagem_rect):
```
Gerencia a tela de instruções do jogo.

**Parâmetros:**
- `jogo`: Estado do jogo
- `tela`: Superfície do Pygame
- `imagem_comojogar`: Imagem das instruções
- `imagem_rect`: Retângulo da imagem

**Retorno:**
- Tupla com estado do jogo e próxima tela

#### game_over_screen
```python
def game_over_screen(screen, final_meters, high_score):
```
Gerencia a tela de Game Over.

**Parâmetros:**
- `screen`: Superfície do Pygame
- `final_meters`: Pontuação final
- `high_score`: Recorde atual

**Retorno:**
- `bool`: True se o jogador escolher reiniciar
