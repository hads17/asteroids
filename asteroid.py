import pygame
import random
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vector1 = self.rotate(random_angle)
        vector2 = self.rotate(-random_angle)

        Asteroid(vector1.position.x, vector1.position.y, self.radius - ASTEROID_MIN_RADIUS)
        Asteroid(vector2.position.x, vector2.position.y, self.radius - ASTEROID_MIN_RADIUS)
