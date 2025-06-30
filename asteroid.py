from constants import *
import pygame
import random
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, radius = self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else: 
            angle = random.uniform(20,50)
            vector_1 = self.velocity.rotate(angle)
            vector_2 = self.velocity.rotate(-angle)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position[0], self.position[1], new_rad)
            ast2 = Asteroid(self.position[0], self.position[1], new_rad)
            ast1.velocity = vector_1 * 1.2
            ast2.velocity = vector_2 * 1.2
        