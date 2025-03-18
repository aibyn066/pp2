import pygame 
pygame.init()

screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
x,y = 375,375

game = True
while game:
    screen.fill('pink')

    pygame.draw.circle(screen,'red',(x,y),25)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 50:
        x -= 20
    if keys[pygame.K_RIGHT] and x < 750:
        x +=20
    if keys[pygame.K_UP] and y > 50 :
        y -= 20
    if keys[pygame.K_DOWN] and y < 750:
        y +=20

    clock.tick(15)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()


