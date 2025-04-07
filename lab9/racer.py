import pygame
import random 
import time

pygame.init()
screen_width, screen_height = 400, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Racer Game")

try:
    road = pygame.image.load("images/AnimatedStreet.png")
    player_car = pygame.image.load("images/Player.png")
    coin_img = pygame.image.load("images/coin.png")
    coin_img = pygame.transform.scale(coin_img, (30, 30)) 
    enemy_car = pygame.image.load("images/Enemy.png")
except Exception as e:
    print(f"Error loading images: {e}")
    pygame.quit()
    exit()

clock = pygame.time.Clock()
road_scroll = 0
base_speed = 5

# границы
BORDERS = {
    'left': 44,
    'right': 312,
    'top': 96,
    'bottom': 504
}

# позиция игрока
player_pos = [180, 504]
player_rect = pygame.Rect(*player_pos, 44, 96)

# Форматы объектов:
# coins - [x, y, weight (1-3)]
# enemies - [x, y]
coins = [] 
enemies = []  

last_coin_spawn = time.time()
last_enemy_spawn = time.time()
SPAWN_DELAY = 2  # секунды спаунов монет и врагов

coin_size = 30
enemy_size = 44
current_enemy_speed = 5
score = 0
speed_increase_threshold = 5  # количество монет для увеличения сложности

font = pygame.font.Font(None, 36)

def spawn_coin():
    x = random.choice([44, 180, 312])  
    weight = random.choices([1, 2, 3], weights=[0.6, 0.3, 0.1])[0]  # 60% шанс для 1, 30% для 2, 10% для 3
    coins.append([x, -coin_size, weight])

def spawn_enemy():
    x = random.choice([44, 180, 312])  
    enemies.append([x, -enemy_size]) # враги спавнятся выше экрана

def increase_difficulty():
    global current_enemy_speed  # работа с глобальной переменной
    if score % speed_increase_threshold == 0 and score > 0: # теперь изменение применится к глобальной переменной
        current_enemy_speed += 1  # увеличиваем скорость врагов

running = True 
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] >= BORDERS['left']:
        player_pos[0] -= 10
    if keys[pygame.K_RIGHT] and player_pos[0] <= BORDERS['right']:
        player_pos[0] += 10
    if keys[pygame.K_DOWN] and player_pos[1] <= BORDERS['bottom']:
        player_pos[1] += 10
    if keys[pygame.K_UP] and player_pos[1] >= BORDERS['top']:
        player_pos[1] -= 10
    
    player_rect.x, player_rect.y = player_pos

    # спавн монет
    if time.time() - last_coin_spawn > SPAWN_DELAY:
        spawn_coin()
        last_coin_spawn = time.time()

    # движение монет
    for coin in coins[:]:
        coin[1] += base_speed  # движение вниз
        
        # проверка на столкновение с игроком
        coin_rect = pygame.Rect(coin[0], coin[1], coin_size, coin_size) # хитбокс монеты
        if player_rect.colliderect(coin_rect):
            score += coin[2]  # увеличиваем счет на вес монеты
            coins.remove(coin)
            increase_difficulty()
    
    # удаляем монеты которые вышли за границы экрана
    coins = [c for c in coins if c[1] < screen_height]

    # спавн врагов
    if time.time() - last_enemy_spawn > SPAWN_DELAY:
        spawn_enemy()
        last_enemy_spawn = time.time()

    for enemy in enemies[:]:
        enemy[1] += current_enemy_speed
        
        # проверка на столкновение с игроком
        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_size, enemy_size) # хитбокс врага
        if player_rect.colliderect(enemy_rect):
            running = False  # Game over
    
    # удаляем врагов которые вышли за границы экрана
    enemies = [e for e in enemies if e[1] < screen_height]

    # движение дороги
    road_scroll += base_speed
    if road_scroll >= screen_height:
        road_scroll = 0
    
    screen.blit(road, (0, road_scroll - screen_height))
    screen.blit(road, (0, road_scroll))
    
    # монеты разных весов
    for x, y, weight in coins:
        if weight == 1:
            screen.blit(coin_img, (x, y))
        elif weight == 2:
            colored_coin = coin_img.copy()
            colored_coin.fill('pink', special_flags=pygame.BLEND_MULT)  # pink
            screen.blit(colored_coin, (x, y))
        else:
            colored_coin = coin_img.copy()
            colored_coin.fill('red', special_flags=pygame.BLEND_MULT)  # red
            screen.blit(colored_coin, (x, y))
    
    # враги
    for x, y in enemies:
        screen.blit(enemy_car, (x, y))
    
    # игрок и отображение счета
    screen.blit(player_car, player_pos)
    score_text = font.render(f"Score: {score}", True, 'white')
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(30)  

pygame.quit()