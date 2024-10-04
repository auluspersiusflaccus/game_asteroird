# this file defines the asteroid class
import pygame
import random
from circleshape import *
from main import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        elif self.radius > ASTEROID_MIN_RADIUS:
            old_radius = self.radius
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            random_angle = random.uniform(20, 50)     
            ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            ast1.velocity = self.velocity.rotate(random_angle) * 1.2
            ast2 = Asteroid(self.position.x, self.position.y, new_radius)
            ast2.velocity = self.velocity.rotate(-random_angle) * 1.2