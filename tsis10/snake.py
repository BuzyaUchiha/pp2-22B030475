import pygame as pg 
import psycopg2
from random import randint, randrange, choice
name = input() 

config = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres", 
    password = "12345"
)
current = config.cursor()
current.execute("""CREATE TABLE IF NOT EXISTS users(
    username VARCHAR(255),
    level INT,
    score INT
);
""")

sql = '''
    SELECT * FROM users WHERE username = %s; 
'''
current.execute(sql, [name])
config.commit()
data = current.fetchone()

if data == None: 
    sql = '''
        INSERT INTO users VALUES(%s, 0, 0);
    '''
    current.execute(sql, [name])
    config.commit()
else: 
    sql = '''
    SELECT level FROM users WHERE username = %s;
    '''
    current.execute(sql, [name])
    final = current.fetchone()
    print(*final)
    config.commit()

pg.init()

w, h, fps, level, step = 800, 800, 4, 0, 40 
screen = pg.display.set_mode((w, h))
pg.display.set_caption('Snake Game')
is_running, lose, paused = True, False, False
clock = pg.time.Clock()
score = pg.font.SysFont("Verdana", 20)
surf = pg.Surface((390, 390))
bg = pg.image.load("/Users/buzyauchiha/pp2-22B030475/tsis10/images/background3.jpg")
bg = pg.transform.scale(bg, (w, h))
gameover = pg.image.load("/Users/buzyauchiha/pp2-22B030475/tsis10/images/game_over.jpg")
gameover = pg.transform.scale(gameover, (390, 390))
cur_sc = 0
pg.mixer.init()
pg.mixer.music.load("/Users/buzyauchiha/pp2-22B030475/tsis10//music/backsound.mp3")
pg.mixer.music.play(-1)
timmer = 5000
rush = False

class Food:
    def __init__(self, im):
      
        self.x = randrange(0, w, step)
        self.y = randrange(0, h, step)
        self.r = 0
        self.image = im

    def draw(self):
        rect = pg.Rect(self.x, self.y, step, step)  
        screen.blit(self.image, rect)
        
    def draw2(self):
        self.x = randrange(0, w, step)
        self.y = randrange(0, h, step)
        self.r = randint(1, 3)
        self.image = pg.image.load(f'/Users/buzyauchiha/pp2-22B030475/tsis10//images/food{self.r}.png')

class Snake:
    def __init__(self):
        self.speed = step
        self.body = [[360, 360]] 
        self.dx = 0
        self.dy = 0
        self.score = 0
        self.color = 'Pink'
    
    def move(self, events):
        for event in events:
            if event.type == pg.KEYDOWN: 
                if event.key == pg.K_a and self.dx == 0: 
                    self.dx = -self.speed
                    self.dy = 0
                if event.key == pg.K_d and self.dx == 0:
                    self.dx = self.speed
                    self.dy = 0
                if event.key == pg.K_w and self.dy == 0:
                    self.dx = 0
                    self.dy = -self.speed
                if event.key == pg.K_s and self.dy == 0:
                    self.dx = 0
                    self.dy = self.speed

        
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0] 
            self.body[i][1] = self.body[i - 1][1]

        
        self.body[0][0] += self.dx 
        self.body[0][1] += self.dy 

    def draw(self):
        for part in self.body:
            pg.draw.rect(screen, self.color, (part[0], part[1], step, step))
    
   
    def collide_food(self, f:Food):
        if self.body[0][0] == f.x and self.body[0][1] == f.y: 
            self.score += f.r 
            pg.mixer.Sound('/Users/buzyauchiha/pp2-22B030475/tsis10/music/eat.mp3').play()
            global rush
            rush = True
            self.body.append([1000, 1000]) 
    
    
    def self_collide(self):
        global is_running
        if self.body[0] in self.body[1:]: 
            lose = True 
            pg.mixer.music.stop()
            pg.mixer.Sound('/Users/buzyauchiha/pp2-22B030475/tsis10/music/gameover.wav').play()
            pg.mixer.music.stop()

 
    def check_food(self, f:Food): 
        if [f.x, f.y] in self.body: 
            f.draw2()


class Wall:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.pic = pg.image.load("/Users/buzyauchiha/pp2-22B030475/tsis10/images/wall2.png")


    def draw(self):
        screen.blit(self.pic, (self.x, self.y))

def disappear(t):
    pg.time.set_timer(pg.USEREVENT, t)


s = Snake()
f = Food(pg.image.load(f'/Users/buzyauchiha/pp2-22B030475/tsis10/images/food{randint(1,3)}.png'))
disappear(5000)

while is_running:
    clock.tick(fps)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            is_running = False
        if event.type == pg.USEREVENT and rush == False: 
            f.draw2() 
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_p: 
                paused = True
    screen.blit(bg, (0, 0))

    my_walls = open(f'wall{level}.txt', 'r').readlines() 
    walls = []
    for i, line in enumerate(my_walls): 
        for j, each in enumerate(line): 
            if each == "+":
                walls.append(Wall(j * step, i * step)) 


    f.draw()
    s.draw()
    s.move(events) 
    s.collide_food(f)
    s.self_collide()
    s.check_food(f)

    
    counter = score.render(f'Score: {s.score}', True, 'black')
    screen.blit(counter, (50, 50))
    l = score.render(f'Level: {level}', True, 'black')
    screen.blit(l, (50, 80))

    
    if s.score >= 3:
        pg.mixer.Sound('/Users/buzyauchiha/pp2-22B030475/tsis10/music/nextlevel.mp3').play()
        level += 1 
        level %= 4 
        fps += 2 
        s.score = 0 
        cur_sc += 3

   
    for wall in walls:
        wall.draw()
        if f.x == wall.x and f.y == wall.y: 
            f.draw2()

        if s.body[0][0] == wall.x and s.body[0][1] == wall.y: 
            lose = True
            pg.mixer.music.stop()
            pg.mixer.Sound('/Users/buzyauchiha/pp2-22B030475/tsis10/music/gameover.wav').play()
            pg.mixer.music.stop()

    if rush == True: 
        timmer = 5000
        disappear(timmer)
        f.draw2() 
        rush = False
    

    while paused: 
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False
                paused = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_u:
                    paused = False 
                if event.key == pg.K_c:
                    a = cur_sc + s.score 
                    sql = '''
                        UPDATE users SET score = %s, level = %s WHERE username = %s;
                    '''
                    current.execute(sql, [a, level, name])
                    config.commit()  
        screen.blit(surf, (200, 200))
        cntr = score.render(f'Your score is {s.score}', True, 'white')
        screen.blit(cntr, (315, 350))
        l = score.render(f'Your level is {level}', True, 'white')
        screen.blit(l, (317, 385))
        txt = score.render(f'Press "C" to save your current state', True, 'white')
        screen.blit(txt, (212, 420))
        pg.display.flip()
        
   
    while lose:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False
                lose = False   
        surf.blit(gameover, (0, 0))
        screen.blit(surf, (200, 200))
        cntr = score.render(f'Your score is {s.score}', True, 'white')
        screen.blit(cntr, (320, 405))
        l = score.render(f'Your level is {level}', True, 'white')
        screen.blit(l, (322, 435))
        pg.display.flip()
        cur_sc += s.score
        l = level

    pg.display.flip()
pg.quit()

sql = '''
    UPDATE users SET score = %s, level = %s WHERE username = %s;
'''
current.execute(sql, [cur_sc, l, name])
config.commit()
current.close()
config.close()
