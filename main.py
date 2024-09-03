import pygame

from asteroid import Asteroid
from constants import *
from player import *
from asteroidfield import AsteroidField



def main():
    
    #VARIABLE CONSTRUCTION SITE
    pygame.init()
    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    #GROUPS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)

    #INITIALISATION
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    asteroid_field = AsteroidField()
    dt = 0

    #GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = (clock.tick(60)) / 1000
        
        for obj in updatable:
            obj.update(dt)

        pygame.Surface.fill(screen, (0,0,0))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()