import pygame
import random


def generate_ball():
   global ball_x
   global ball_y
   ball_x = random.randint(0,WIDTH)
   ball_y = random.randint(0,HEIGHT)
   red = random.randint(0,255)
   green = random.randint(0,255)
   blue = random.randint(0,255)
   pygame.draw.circle(
       main_screen,
       (red,green,blue),
       (ball_x, ball_y),
       20
   )
   pygame.display.update()


WIDTH = 800
HEIGHT = 800

pygame.init()
main_screen=pygame.display.set_mode((WIDTH,HEIGHT))

ball_x = ball_y = 0

while True:
    generate_ball()
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEMOTION:
            pass
    pygame.display.update()