import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # fps vars
    clock = pygame.time.Clock()
    dt = 0

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
        player.update(dt)
        player.draw(screen)
        
        
        # end of loop logic
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
  
    

if __name__ == "__main__":
    main()
