import pygame
from constants import *

def main():
     pygame.init()
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



          pygame.display.flip()

if __name__ == "__main__":
     main()
