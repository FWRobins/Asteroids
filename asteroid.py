import pygame
import random

from circleshape import CircleShape

from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            random_angle = random.uniform(20, 50)
            v1 = self.velocity.rotate(random_angle)
            v2 = self.velocity.rotate(-random_angle)
            radius = self.radius - ASTEROID_MIN_RADIUS
            baby_asteroid1 = Asteroid(self.position[0], self.position[1], radius)
            baby_asteroid1.velocity = v1*1.2
            baby_asteroid2 = Asteroid(self.position[0], self.position[1], radius)
            baby_asteroid2.velocity = v2*1.2
            self.kill()
