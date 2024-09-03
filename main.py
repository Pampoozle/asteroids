import pygame

from constants import *
from player import *


def main():
    #VARIABLE CONSTRUCTION SITE
    pygame.init()
    clock = pygame.time.Clock()
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        dt = (clock.tick(60)) / 1000
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        clock.tick(60)
        
        
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()