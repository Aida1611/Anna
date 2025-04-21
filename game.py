import pygame
pygame.init()

display = pygame.display.set_mode((700, 400))
pygame.display.set_caption('Hi this my first game')
icon = pygame.image.load('image/maska.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('image/fon3.jpg')
square = pygame.Surface((150, 175))
player_right = [
    pygame.image.load('image/right1.png'),
    pygame.image.load('image/right2.png'),
    pygame.image.load('image/right3.png'),
    pygame.image.load('image/right4.png'),
    pygame.image.load('image/right5.png'),
    pygame.image.load('image/right6.png'),
    pygame.image.load('image/right7.png')
    ]

player_count = 1
#square.fill('red')
run = True
while run:

    display.fill((30,129,176))
    display.blit(square, (50, 260))
    display.blit(bg, (0, 0))
    display.blit(player_right [player_count], (200, 250))

    if player_count == 3:
        player_count = 0
    else:
        player_count += 1

  
    

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.guit()
        elif event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_a:
                display.fill((255, 255, 255))


