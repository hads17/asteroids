# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()

   # Gameloop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for u in updatable:
            u.update(dt)

        for a in asteroids:
            if (a.collisionCheck(player) == True):
                print("Game Over")
                sys.exit()
            for s in shots:
                if(s.collisionCheck(a) == True):
                    a.split()
                    s.kill()
             
        screen.fill("black")

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()


