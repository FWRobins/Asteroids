import pygame

from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED
from constants import SHOT_RADIUS
from circleshape import CircleShape
from shots import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
        
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        #rotate counter clockwise
        if keys[pygame.K_a]:
            self.rotate(-dt)
        
        #rotate clockwise
        if keys[pygame.K_d]:
            self.rotate(dt)

        #rotate backwards
        if keys[pygame.K_s]:
            self.move(-dt)

        #rotate forwards
        if keys[pygame.K_w]:
            self.move(dt)

        #shoot
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def shoot(self):
        shot = Shot(self.position[0], self.position[1], SHOT_RADIUS)
        #setup base direction with vector2, modify with player rotation, add speed
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation)*PLAYER_SHOOT_SPEED
