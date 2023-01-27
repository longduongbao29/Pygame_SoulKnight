from Game import Game

import pygame
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()

mainScreen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Soul Knight by Long')
pygame.display.set_icon(pygame.image.load('assets\icon\icon.png'))

clock = pygame.time.Clock()

running = True
game = Game()
while game.running:
    mainScreen.fill('white')
    clock.tick(60)
    game.handleEvent()
    game.player.update()
    game.player.draw()
    pygame.display.flip()


pygame.quit()
sys.exit()
