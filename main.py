import sys
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH,SCREEN_HEIGHT 
from logger import log_state,log_event




def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH},Screen height: {SCREEN_HEIGHT}")


    # Initialize all imported pygame modules
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    dt = 0.0

    # Create sprite groups for updatable and drawable playable objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # Create sprite groups for updatable and drawable asteroids objects
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable,) 
    asteroidfield = AsteroidField()
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        log_state()
        screen.fill('black')  # Clear the screen with black before drawing each frame

        for obj in updatable:
            obj.update(dt)  # Update the player's state based on input and delta time

        for obj in drawable:
            obj.draw(screen)     # Draw all drawable objects on the screen

        for obj in asteroids:
            if obj.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        
        pygame.display.flip()  # Update the full display surface to the screen

        for event in pygame.event.get():
            pass
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        dt = clock.tick(60) / 1000.0  # Limit to 60 FPS and get delta time in seconds
        # print(f"Delta time for this frame: {dt}")


if __name__ == "__main__":
    main()
