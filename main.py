from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
import pygame
import sys

from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)

    AsteroidField.containers = (updatable)

    clock = pygame.time.Clock()
    dt = 0

    field = AsteroidField()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for up in updatable:
            up.update(dt)

        for dr in drawable:
            dr.draw(screen)

        pygame.display.flip()

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()


        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
