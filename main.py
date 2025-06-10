import pygame
import random



WIDTH = 800
HEIGHT = 800


pygame.init()
main_screen=pygame.display.set_mode((WIDTH,HEIGHT))

while True:
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEMOTION:
            x=event.pos[0]
            y=event.pos[1]
            pygame.draw.circle(
                main_screen,
                (0,255,255),
                (x,y),
                10,
            )
    pygame.display.update()