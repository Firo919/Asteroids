import pygame
from player import *
from constants import *

def main():
     pygame.init()
     Clock = pygame.time.Clock()
     player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
     dt = 0
     print("Starting Asteroids!")
     print(f"Screen width: {SCREEN_WIDTH}")
     print(f"Screen height: {SCREEN_HEIGHT}")

     screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
     Black = (0,0,0)
     x = 0
     while(x < 1):
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    return
          screen.fill(Black)
          player.update(dt)
          player.draw(screen)

          Clock.tick(60)
          dt = Clock.tick(60)/1000
          pygame.display.flip()
          

if __name__ == "__main__":
     main()
