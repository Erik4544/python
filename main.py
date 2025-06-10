import pygame
import random


def generate_ball():
   global ball_x
   global ball_y
   ball_x = random.randint(0,WIDTH)
   ball_y = random.randint(0,HEIGHT)
   red = random.randint(100,255)
   green = random.randint(100,255)
   blue = random.randint(100,255)
   pygame.draw.circle(
       main_screen,
       (red,green,blue),
       (ball_x, ball_y),
       20
   )
   pygame.display.update()

score=0
WIDTH = 800
HEIGHT = 800

pygame.init()
main_screen=pygame.display.set_mode((WIDTH,HEIGHT))

ball_x = ball_y = 0

clock = pygame.time.Clock()

while True:
    main_screen.fill((0,0,0))
    clock.tick(1)
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x=event.pos[0]
            mouse_y=event.pos[1]
            print(mouse_x, mouse_y)
            if ball_x - 20 <=mouse_x <= ball_x + 20 and ball_y - 20 <=mouse_y <= ball_y + 20:
                score+=1



    generate_ball()
    pygame.display.update()