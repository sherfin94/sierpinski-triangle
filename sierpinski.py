import pygame, math, random
from pygame.locals import *
color = (255,255, 255)
screen = pygame.display.set_mode((640, 700), RESIZABLE)
running = 1

def triangle(p1,p2,p3, myColor):
  #sleep(5)
  pygame.draw.line(screen,myColor,p1,p2)
  pygame.draw.line(screen,myColor,p2,p3)
  pygame.draw.line(screen,myColor,p3,p1)


def midpoint(p1,p2):
  return ((p1[0] + p2[0])/2.0, (p1[1] + p2[1])/2.0)

def gen(p1,p2,p3,d):
  if d <= 0:
    return 0
  else:

    mp1 = midpoint(p1,p3)
    mp2 = midpoint(p2,p3)
    mp3 = midpoint(p1,p2)

    #print mp3,mp1,mp2
    myColor = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    triangle(mp1, mp2, mp3, myColor)

    gen(p1, mp3, mp1, d - 1)
    gen(mp3, p2, mp2, d - 1)
    gen(mp1, mp2, p3, d - 1)

    #return 0

p1 = (0 ,0)
p2 = (640, 0)
p3 = (320, math.sqrt(640*640 - 320*320))

clock = pygame.time.Clock()
clock.tick(5)

flag = True
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
         running = 0
    screen.fill((255, 255, 255))
    triangle(p1, p2, p3, color)
    gen(p1, p2, p3, 10)

    #pygame.draw.line(screen, (0, 0, 255), (0, 0), (639, 479))
    #pygame.draw.aaline(screen, (0, 0, 255), (639, 0), (0, 479))
    pygame.display.flip()
