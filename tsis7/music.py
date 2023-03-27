import pygame

pygame.init()
song_list = [
   "Eraser.mp3", "CastleOnTheHill.mp3", "Dive.mp3", 
   "ShapeofYou.mp3", "Perfect.mp3", "GalwayGirl.mp3", 
   "Happier.mp3", "NewMan.mp3", "HeartsDont.mp3", 
   "WhatDoIKnow.mp3", "HowWouldYouFeel.mp3", "SupermarketFlowers.mp3", 
   "Barcelona.mp3", "BibiaBeYEYE.mp3", "NancyMulligan.mp3"
    ]
song_names = [
   "Eraser", "Castle On The Hill", "Dive", 
   "Shape of You", "Galway Girl", "Happier", 
   "New Man", "Hearts Dont Break Around Here", 
   "What Do I Know?", "How Would You Feel", "Supermarket Flowers", 
   "Barcelona", "Bibia Be Ye Ye", "Nancy Mulligan"
    ]
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption('÷')

font = pygame.font.SysFont('sf', 24)
clock = pygame.time.Clock()
running = True

index = 0
pygame.mixer.music.load(song_list[index])
pygame.mixer.music.play()
song_name = song_names[index]
text = font.render("Currently playing:  ", True, ('black'))
text1 = font.render(song_name, True, ('black'))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        index -= 1
        pygame.mixer.music.load(song_list[index])
        song_name = song_names[index]
        text = font.render("Currently playing:  ", True, ('black'))
        text1 = font.render(song_name, True, ('black'))
        pygame.mixer.music.play()
    if pressed[pygame.K_SPACE]: pygame.mixer.music.stop()
    if pressed[pygame.K_UP]: pygame.mixer.music.pause()
    if pressed[pygame.K_DOWN]: pygame.mixer.music.unpause()
    if pressed[pygame.K_RIGHT]: 
        index += 1
        pygame.mixer.music.load(song_list[index])
        song_name = song_names[index]
        text = font.render("Currently playing:  ", True, ('black'))
        text1 = font.render(song_name, True, ('black'))
        pygame.mixer.music.play()
    if index == len(song_list) - 1:
        index = -1


    screen.fill((255, 255, 255))
    screen.blit(pygame.image.load('Divide.jpg'), (0, 0))
    screen.blit(text, (400, 535))
    screen.blit(text1, text1.get_rect(center = (470,565)))
    pygame.display.flip()
    clock.tick(5.75)