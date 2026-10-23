import pygame
from logger import log_state
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))

        pygame.display.flip()



if __name__ == "__main__":
    main()
