import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(surface=screen, color='white', center=self.position, radius=self.radius, width=LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position = self.position + (self.velocity * dt)

    def split(self) -> None:
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            first_velocity = self.velocity.rotate(angle)
            second_velocity = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid.velocity = first_velocity * 1.2
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2.velocity = second_velocity * 1.2
            return [new_asteroid, new_asteroid2]
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        return
    
    