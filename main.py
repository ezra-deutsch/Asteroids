import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT 
from logger import log_state



def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH},Screen height: {SCREEN_HEIGHT}")


    # Initialize all imported pygame modules
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        screen.fill('black')  # Clear the screen with black before drawing each frame
        pygame.display.flip()  # Update the full display surface to the screen
        for event in pygame.event.get():


            pass
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == "__main__":
    main()
