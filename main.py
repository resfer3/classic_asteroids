import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # fps vars
    clock = pygame.time.Clock()
    dt = 0

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # asteroid init
    asteroid_field = AsteroidField()

    # player vars
    x = SCREEN_WIDTH / 2 
    y = SCREEN_HEIGHT / 2
    player = Player(x, y, PLAYER_RADIUS)

        # game loop
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, "black")
        updatable.update(dt)
        # if plane crashes, game over
        for asteroid in asteroids:
            if player.collision(asteroid) == True:
                print("Game Over")
                sys.exit(1)
        # if hit by bullet, asteroid disappear
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collision(asteroid) == True:
                    asteroid.split()
                    bullet.kill()
        # generate sprites
        for obj in drawable:
            obj.draw(screen)
        
        
        # end of loop logic
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
  
    

if __name__ == "__main__":
    main()
