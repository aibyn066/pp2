import pygame

pygame.init()

screen = pygame.display.set_mode((411,709))
image = pygame.image.load('images/background_music.jpg')
screen.blit(image,(0,0))
musics = ['musics/music1.mp3','musics/music2.mp3','musics/music3.mp3']
images = ['images/image1.jpg','images/image2.jpg','images/image3.jpg']
running = True
cnt = 0
while running:

    screen.blit(image,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pygame.mixer.music.load(musics[cnt])
                pygame.mixer.music.play()
                image = pygame.image.load(images[cnt])    

            elif event.key == pygame.K_SPACE:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_RIGHT:
                cnt +=1
                if cnt > 2:
                    cnt = 0
        
                pygame.mixer.music.load(musics[cnt])
                pygame.mixer.music.play()
                image = pygame.image.load(images[cnt])    
                
            elif event.key == pygame.K_LEFT:
                go = True
                if cnt == 0 :
                    go = False
                    pygame.mixer.music.stop()
                if go:
                    cnt -= 1
                    pygame.mixer.music.load(musics[cnt])
                    pygame.mixer.music.play()
                    image = pygame.image.load(images[cnt]) 
    pygame.display.update()

                

                


