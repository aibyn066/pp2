import pygame
import datetime


pygame.init()

screen = pygame.display.set_mode((800,600))
screen.fill('white')
watch = pygame.image.load('images/clock.png')
right = pygame.image.load('images/sec_hand.png')
left = pygame.image.load('images/min_hand.png')


running = True
while running:

    pygame.display.update()
    screen.blit(watch,(0,0))
    date = datetime.datetime.now()
    seconds = date.second  
    minutes = date.minute
    

    angle = (-seconds * 6) + 60  
    angle_min = (-minutes*6) - 60
    

    rotated_right = pygame.transform.rotate(right, angle)
    rotated_left = pygame.transform.rotate(left,angle_min)
    

    rect_right = rotated_right.get_rect(center=(400,300))
    rect_left = rotated_left.get_rect(center=(400,300))
    

    screen.blit(rotated_right, rect_right.topleft)
    screen.blit(rotated_left,rect_left.topleft)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()