import pygame, sys

import SpaceShip_Game
from SpaceShip_Game import spaceship_group, meteor_group, laser_group, Laser, generate_rand_meteor, spaceship

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

METEOR_EVENT = pygame.USEREVENT
pygame.time.set_timer(METEOR_EVENT,100)

while True: #Game Loop
    for event in pygame.event.get(): # Check for events from user
        if event.type == pygame.QUIT: #close the game
            pygame.quit()
            sys.exit()

        if event.type == METEOR_EVENT:
            generate_rand_meteor()

        if event.type == pygame.MOUSEBUTTONDOWN:
            laser = Laser("images\laser.png", pygame.mouse.get_pos(), 15)
            laser_group = pygame.sprite.Group()
            laser_group.add(laser)



    screen.fill((42,45,51)) # Set background colour

    for index, shield in enumerate(range(SpaceShip_Game.spaceship.health )):
        screen.blit(spaceship.shield_surface, (index * 40, 10))

    spaceship_group.draw(screen) #Draw spaceship
    meteor_group.draw(screen)
    laser_group.draw(screen)
    spaceship_group.update()
    meteor_group.update()
    laser_group.update()
    pygame.display.update() #Draw frame
    clock.tick(120) #Control the framerate
