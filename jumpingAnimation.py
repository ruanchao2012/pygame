import pygame,time
from pygame.locals import *

class MySprite(pygame.sprite.Sprite):
    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self)
        self.master_image = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0

    # X property
    def _getx(self): return self.rect.x
    def _setx(self, value): self.rect.x = value
    X = property(_getx,_setx)

    # Y property
    def _gety(self): return self.rect.y
    def _sety(self, value): self.rect.y = value
    Y = property(_gety,_sety)

    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = Rect(0,0,width,height)
        self.columns = columns

        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1 # calculate total frames according to the size of one frame

    def update(self, current_time, rate = 900): # rate: how many ticks each frame
        #update animation frame number
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        #build current frame only if it changed
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame

    def __str__(self):
        return str(self.frame) + "," + str(self.first_frame) + \
               "," + str(self.last_frame) + "," + str(self.frame_width) + \
               "," + str(self.frame_height) + "," + str(self.columns) + \
               "," + str(self.rect)


def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

SCREEN_LEN = 120
SCREEN_HIGH = 260


pygame.init()
screen = pygame.display.set_mode((SCREEN_LEN,SCREEN_HIGH), 0, 32)
#myfont = pygame.font.Font(None,60)
myfont=pygame.font.SysFont('arial',18)
pygame.display.set_caption("Sprite Animation Demo")

framerate = pygame.time.Clock()

#create the dragon sprite
dragon = MySprite(screen)
#dragon.load("dragon.png", 260, 150, 3)
#dragon.load("./rc/time.jpg", 1200, 520, 10)
dragon.load("./rc/jumping animation.jpg", 120, 260, 10)

group = pygame.sprite.Group()
group.add(dragon)

while True:
    framerate.tick(30) # system frame rate
    ticks = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        sys.exit()

    screen.fill((0,0,100))
    group.update(ticks)
    group.draw(screen)
    print_text(myfont, 0, 0, "Sprite: " + str(dragon))
    pygame.display.update()

