import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'white'
    points = []
    font = pygame.font.SysFont('Times New Roman', 14)
    red_color = font.render('Click R for red, G for green, B for blue', True, (255, 0, 0))
    
    class Button:
        def __init__(self, x, y, width, height, image):
            self.rect = pygame.Rect(x, y, width, height)
            self.image = image


    while True:
        
        pressed = pygame.key.get_pressed()
        
        command_held = pressed[pygame.K_LMETA] or pressed[pygame.K_RMETA]
        
        for event in pygame.event.get():
        
            # determine if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and command_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed 
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    mode = 'black'
                elif event.key == pygame.K_p:
                    mode = 'pink'
                elif event.key == pygame.K_n:
                    mode = 'neon'
                elif event.key == pygame.K_w:
                    mode = 'white'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius 
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list 
                position = event.pos
                points = points + [position]
                points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        # draw all points 
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    c3 = max(0, min(255, 2 * index - 128))
    c4 = max(0, min(255, 2 * index - 221))
    c5 = max(0, min(255, 2 * index - 31))
    c6 = max(0, min(255, 2 * index - 25))
             
             
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'black':
        color = (0, 0, 0)
    elif color_mode == 'pink':
        color = (c3, c1, c3)
    elif color_mode == 'neon':
        color = (c5, c6, c4)
    elif color_mode == 'white':
        color = (255, 255, 255)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()