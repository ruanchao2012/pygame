import sys
import pygame,time
from pygame.locals import *
import random

SCREEN_LEN = 400
SCREEN_HIGH = 500

class Bomb:
    def __init__(self,color=(255,255,0),pos_x=SCREEN_LEN/2, pos_y=0, radius=20, width=0):
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = radius
        self.width = width

    def move(self, x=0, y=1):
        self.pos_x = self.pos_x + x
        self.pos_y = self.pos_y + y

        global isCatched, isExploded
        if (True == isExploded or True == isCatched): # runs outside the screen, or collides with sheild
            self.pos_x = int(random.random() * SCREEN_LEN)  # random.random() returns [0,1)
            self.pos_y = 0

    def setPos(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def draw(self, screen):
        pygame.draw.circle(screen,self.color,(self.pos_x,self.pos_y),self.radius,self.width)


class Shield:
    def __init__(self,color=(255,0,0),pos_x=SCREEN_LEN/2, pos_y=SCREEN_HIGH-100, length=100, high=10, width=0):
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.length = length
        self.high = high
        self.width = width

    def move(self, x, y=0):
        self.pos_x = self.pos_x + x
        self.pos_y = self.pos_y + y

        if (self.pos_x + self.length > SCREEN_LEN):
            self.pos_x = SCREEN_LEN - self.length
        elif(self.pos_x <0):
            self.pos_x = 0

        if (self.pos_y > SCREEN_HIGH):
            self.pos_y = SCREEN_HIGH
        elif(self.pos_y <0):
            self.pos_y = 0

    def setPos(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.pos_x,self.pos_y,self.length,self.high), self.width)

bombExist = False
isCatched = False # it can be a member of class Bomb
isExploded = False # it can be a member of class Bomb
#bomb_vel_x = 0  # move speed
#bomb_vel_y = 1  # move speed

bomb = Bomb()
shield = Shield()

def checkIfCatched(bomb, shield):
    global isCatched
    #if (bomb.pos_x + bomb.radius)>shield.pos_x and (bomb.pos_x + bomb.radius)<(shield.pos_x+shield.length) and (bomb.pos_y+bomb.radius*2)==shield.pos_y:
    if bomb.pos_x > shield.pos_x and bomb.pos_x < (shield.pos_x + shield.length) and (bomb.pos_y + bomb.radius) == shield.pos_y:
        isCatched = True
    else:
        isCatched = False
    return isCatched

def checkIfExploded(bomb):
    global isExploded
    if bomb.pos_y > SCREEN_HIGH-bomb.radius:
        isExploded = True
    else:
        isExploded = False
    return isExploded


pygame.init()
screen = pygame.display.set_mode((SCREEN_LEN,SCREEN_HIGH))
#myfont = pygame.font.Font(None,60)
myfont=pygame.font.SysFont('arial',36)
pygame.display.set_caption("Bomb Catcher")

audio_clip = pygame.mixer.Sound("./rc/explosion.wav")
audio_channel = pygame.mixer.find_channel(True)

while(True):
    screen.fill((0, 0, 200))
    time.sleep(0.003)

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    ret = checkIfCatched(bomb,shield)
    if ret == True:
        time.sleep(0.5)

    ret = checkIfExploded(bomb)
    if ret == True:
        audio_channel.play(audio_clip)
        time.sleep(0.5)


    keys = pygame.key.get_pressed() # keyboard
    if keys[K_ESCAPE]:
        sys.exit()
    if keys[K_LEFT]:
        shield.move(-1, 0)
    if keys[K_RIGHT]:
        shield.move(1, 0)

#    if(bomb.pos_y > 600):
#        bomb.setPos(int(random.random()*600), 50) # random.random() returns [0,1)
    bomb.move()

    bomb.draw(screen)
    shield.draw(screen)

    pygame.display.update()
