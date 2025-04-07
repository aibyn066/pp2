import pygame
import sys
import math

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Advanced Paint")

# параметры рисования
current_color = 'BLACK'
brush_size = 5
drawing = False
last_pos = None
start_pos = None
mode = "brush"  # мод по умолчанию

screen.fill('WHITE')

def draw_right_triangle(surface, color, start, end, width=2):
    points = [
        start,
        (start[0], end[1]),
        end
    ]
    pygame.draw.polygon(surface, color, points, width)

def draw_equilateral_triangle(surface, color, start, end, width=2):
    height = end[1] - start[1]
    side_length = abs(end[0] - start[0])
    
    # вычисляем координаты вершин равностороннего треугольника
    top = (start[0] + side_length // 2, start[1])
    left = (start[0], end[1])
    right = (end[0], end[1])
    
    pygame.draw.polygon(surface, color, [top, left, right], width)

def draw_rhombus(surface, color, start, end, line_width=2):
    center_x = (start[0] + end[0]) // 2
    center_y = (start[1] + end[1]) // 2
    rhombus_width = abs(end[0] - start[0]) // 2
    height = abs(end[1] - start[1]) // 2
    
    points = [
        (center_x, center_y - height),  # верх
        (center_x + rhombus_width, center_y),   # право
        (center_x, center_y + height),  # низ
        (center_x - rhombus_width, center_y)    # лево
    ]
    pygame.draw.polygon(surface, color, points, line_width)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # цвета
            if event.key == pygame.K_1: current_color = 'BLUE'
            elif event.key == pygame.K_2: current_color = 'GREEN'
            elif event.key == pygame.K_3: current_color = 'RED'
            
            # изменение режима рисования
            elif event.key == pygame.K_b: mode = "brush"
            elif event.key == pygame.K_e: mode = "eraser"
            elif event.key == pygame.K_c: mode = "circle"
            elif event.key == pygame.K_r: mode = "rect"
            elif event.key == pygame.K_s: mode = "square"
            elif event.key == pygame.K_t: mode = "rtriangle"  
            elif event.key == pygame.K_y: mode = "etriangle"  
            elif event.key == pygame.K_h: mode = "rhombus"
            elif event.key == pygame.K_q: screen.fill('WHITE')  

        # мышь нажата - начать рисование
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            last_pos = event.pos

        # мышь отпущена - закончить рисование
        if event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end_pos = event.pos
                
                # рисование в зависимости от режима
                if mode == "rect":
                    rect = pygame.Rect(
                        min(start_pos[0], end_pos[0]), 
                        min(start_pos[1], end_pos[1]),
                        abs(start_pos[0] - end_pos[0]), 
                        abs(start_pos[1] - end_pos[1])
                    )
                    pygame.draw.rect(screen, current_color, rect, width=2)
                
                elif mode == "square":
                    size = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    rect = pygame.Rect(
                        start_pos[0], 
                        start_pos[1], 
                        size, 
                        size
                    )
                    pygame.draw.rect(screen, current_color, rect, width=2)
                
                elif mode == "circle":
                    radius = int(((start_pos[0] - end_pos[0]) ** 2 + (start_pos[1] - end_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, current_color, start_pos, radius, width=2)
                
                elif mode == "rtriangle":
                    draw_right_triangle(screen, current_color, start_pos, end_pos, 2)
                
                elif mode == "etriangle":
                    draw_equilateral_triangle(screen, current_color, start_pos, end_pos, 2)
                
                elif mode == "rhombus":
                    draw_rhombus(screen, current_color, start_pos, end_pos, 2)
            
            drawing = False

        # движение мыши - рисование
        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == "brush":
                pygame.draw.line(screen, current_color, last_pos, event.pos, brush_size)
                last_pos = event.pos
            elif mode == "eraser":
                pygame.draw.line(screen, 'WHITE', last_pos, event.pos, brush_size * 2)
                last_pos = event.pos

    # инструкции
    font = pygame.font.SysFont(None, 24)
    instructions = [
        "1: Blue | 2: Green | 3: Red",
        "B: Brush | E: Eraser | Q: Clear",
        "C: Circle | R: Rectangle | S: Square",
        "T: Right Triangle | Y: Equilateral Triangle | H: Rhombus"
    ]
    
    for i, text in enumerate(instructions):
        text_surface = font.render(text, True, 'BLACK')
        screen.blit(text_surface, (10, 10 + i * 25))

    pygame.display.update()