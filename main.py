import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT 
from logger import log_state



def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH},Screen height: {SCREEN_HEIGHT}")


    # Initialize all imported pygame modules
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    dt = 0.0

    # Game loop
    while True:
        log_state()
        screen.fill('black')  # Clear the screen with black before drawing each frame
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
