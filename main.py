import pygame
from player import *
from asteroid import *
from constants import *
from asteroidfield import *

def main():
     pygame.init()
     Clock = pygame.time.Clock()
     updatable = pygame.sprite.Group()
     drawable = pygame.sprite.Group()
     asteroids = pygame.sprite.Group()
     shots = pygame.sprite.Group()

     AsteroidField.containers = updatable
     Player.containers = (updatable, drawable)
     Asteroid.containers = (asteroids, updatable, drawable)
     Shot.containers = (shots, updatable, drawable)

     asteroidfield = AsteroidField()
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
               
          updatable.update(dt)

          for obj in asteroids:
               if player.checkCollision(obj) is True:
                    print("Game Over!")
                    return
               for shot in shots:
                    if obj.checkCollision(shot) is True:
                         obj.kill()
                         shot.kill()
                     

          screen.fill(Black)
          
          for drawables in drawable:
               drawables.draw(screen)

          Clock.tick(60)
          dt = Clock.tick(60)/1000
          pygame.display.flip()
          keys = pygame.key.get_pressed()
          if keys[pygame.K_ESCAPE]:
               return
          

if __name__ == "__main__":
     main()
