import pygame 
import random 

pygame.init()
cell_size = 10
width, height = 600, 400  # Увеличил поле для более комфортной игры
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("snake")

# Инициализация змейки
snake = [(100, 100), (90, 100), (80, 100)]
direction = (cell_size, 0)
next_direction = direction

# Генерация еды
def create_food():
    while True:
        x = random.randrange(0, width, cell_size)
        y = random.randrange(0, height, cell_size)
        if (x, y) not in snake:
            return (x, y)

food = create_food()
gold_food = None
gold_time = 0

# Основные параметры
score = 0
speed = 8
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 25)

running = True
while running:
    # Обработка управления
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, cell_size):
                next_direction = (0, -cell_size)
            elif event.key == pygame.K_DOWN and direction != (0, -cell_size):
                next_direction = (0, cell_size)
            elif event.key == pygame.K_LEFT and direction != (cell_size, 0):
                next_direction = (-cell_size, 0)
            elif event.key == pygame.K_RIGHT and direction != (-cell_size, 0):
                next_direction = (cell_size, 0)
    
    direction = next_direction
    
    # Движение змейки
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])
    snake.insert(0, new_head)
    
    # Проверка на съедение еды
    if new_head == food:
        score += 1  # Увеличиваем счет
        food = create_food()
        speed += 1  # Увеличиваем скорость при поедании еды
        
        # С шансом 20% появляется золотая еда
        if random.random() < 0.20:
            gold_food = create_food()
            gold_time = pygame.time.get_ticks()
    
    elif gold_food and new_head == gold_food:
        score += 3  # Увеличиваем счет при поедании золотой еды
        gold_food = None
        speed += 1.5  # Увеличиваем скорость при поедании золотой еды
    else:
        snake.pop()  # Если не съели еду - укорачиваем хвост
    
    # Золотая еда исчезает через 8 секунды
    if gold_food and pygame.time.get_ticks() - gold_time > 8000:
        gold_food = None
        
    # Проверка на столкновение
    # if (new_head[0] < 0 or new_head[0] >= width or
    #     new_head[1] < 0 or new_head[1] >= height or
    #     new_head in snake[1:]):
    #     running = False 
    
    # Телепортация при выходе за границы
    head_x, head_y = new_head
    if head_x >= width:
        head_x = 0
    elif head_x < 0:
        head_x = width - cell_size
    if head_y >= height:
        head_y = 0
    elif head_y < 0:
        head_y = height - cell_size
    
    new_head = (head_x, head_y)
    snake[0] = new_head
    
    # Проверка на столкновение с собой
    if new_head in snake[1:]:
        running = False
        
    # Отрисовка
    screen.fill("#a8d8a8")  # Приятный зеленый фон
    
    # Рисуем змейку
    for segment in snake:
        pygame.draw.rect(screen, "#2a5c2a", (*segment, cell_size, cell_size))
    
    # Рисуем еду
    pygame.draw.rect(screen, "#c62828", (*food, cell_size, cell_size))
    if gold_food:
        pygame.draw.rect(screen, "#f9d71c", (*gold_food, cell_size, cell_size))
    
    # Выводим счет
    score_text = font.render(f"scores: {score}", True, "black")
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()