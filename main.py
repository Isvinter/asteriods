import os
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from constants import *
from player import *
from asteroids import *
from asteroidfield import *


def main():
    
    pygame.init()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = (updatable)
    
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    
    asteroid_field = AsteroidField()
    
    time_object = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        
        for entity in drawable:
            entity.draw(screen)
            
        updatable.update(dt)
        
        #collision check
        for asteroid in asteroids:
            if player.collision_check(asteroid):
                print("Game Over!")
                sys.exit()
                
        for shot in shots:
             for asteroid in asteroids:
                 if shot.collision_check(asteroid): 
                    shot.kill()  
                    asteroid.split()
                    asteroid.kill()
        
        delta_time = time_object.tick(60)
        dt = delta_time / 1000
        
        pygame.display.flip()
   
        
    #print("Starting Asteroids!")
    #print(f"""Screen width: {SCREEN_WIDTH}
#Screen height: {SCREEN_HEIGHT}""")

if __name__ == "__main__":
    main()