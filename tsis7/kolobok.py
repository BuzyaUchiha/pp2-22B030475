import pygame
pygame.init()
screen_width = 1280
screen_height = 800
screen = pygame.display.set_mode((1280, 800))
x = 50
y = 50

color = ((255, 255, 255 ))

running = True

clock = pygame.time.Clock()
pygame.display.set_caption('drawing circle')
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y-=40
    if pressed[pygame.K_DOWN]: y+=40
    if pressed[pygame.K_LEFT]: x-=40
    if pressed[pygame.K_RIGHT]: x+=40

    if x <= 50:
        x = 50
    elif x >= 1230:
        x = 1230
    if y <= 50:
        y = 50
    elif y >= 750:
        y = 750
    

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, color, (x, y), 50)

    pygame.display.flip()
    clock.tick(25)