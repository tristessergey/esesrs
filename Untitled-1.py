
from pygame import *
'''Необходимые классы'''
 
#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (65, 65))
       self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
    
class Hero(GameSprite):
    def forward(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
  
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
        self.direction = 'left'
    def forward(self):
        if self.rect.x >= 650:
            self.direction = 'left'
        if self.rect.x <= 50:
            self.rect.x = 100
            self.direction = 'right'
        if self.direction == 'right':
            self.rect.x += self.speed
        if self.direction == 'left':
            self.rect.x -= self.speed
    
class Wall(sprite.Sprite):
    def __init__(self, c1, c2, c3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.wall_width = wall_width
        self.wall_height = wall_height
        self.image = Surface((self.wall_width, self.wall_height))
        self.image.fill((c1, c2, c3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

 
#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))
 
#Персонажи игры:
player = Hero('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)
 
game = True
clock = time.Clock()
FPS = 60
 
#музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
 
while game:
   for e in event.get():
       if e.type == QUIT:
           game = False
  
   window.blit(background,(0, 0))
   player.forward()
   player.reset()

   monster.forward()
   monster.reset()
   
 
   display.update()
   clock.tick(FPS)
