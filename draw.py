import pygame,time
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,600))
myfont = pygame.font.Font(None,60)
pygame.display.set_caption("Drawing Circles")
#textImage = myfont.render("Hello Pygame", True, white)

pox_x = 300
pox_y = 300
radius = 100
vel_x = 1
vel_y = 2

length = 100
high = 100
pox_x_rect = 300
pox_y_rect = 300
vel_x_rect = -1
vel_y_rect = -2

width = 5  # width = 0


while(True):
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0,0,200))
    color = 255,255,0

    pos = pox_x,pox_y
    pygame.draw.circle(screen,color,pos,radius,width)

    pos_rect = pox_x_rect,pox_y_rect,length,high
    width = 5
    pygame.draw.rect(screen,color,pos_rect,width)

    #screen.blit(textImage, (100, 100))
    pygame.display.update()

    if pox_x > 600 or pox_x < 0:
        vel_x = -vel_x

    if pox_y > 600 or pox_y <0:
        vel_y = -vel_y

    if pox_x_rect > 600 or pox_x_rect < 0:
        vel_x_rect = -vel_x_rect

    if pox_y_rect > 600 or pox_y_rect <0:
        vel_y_rect = -vel_y_rect

    pox_x += vel_x
    pox_y += vel_y
    pox_x_rect += vel_x_rect
    pox_y_rect += vel_y_rect


