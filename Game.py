import pygame
from enum import Enum
from AssetsManager import AssetsManager
from Player import Player


assetsManager = AssetsManager()


class Direction(Enum):
    LEFT = 'Left'
    RIGHT = 'Right'


class Game(object):
    def __init__(self):
        self.running = True
        self.player = Player(300, 300)

    def handleEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.player.isMoving = True
                    self.player.direct = Direction.LEFT
                elif event.key == pygame.K_d:
                    self.player.isMoving = True
                    self.player.direct = Direction.RIGHT
            elif event.type == pygame.KEYUP:
                self.player.isMoving = False
                self.player.idle()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.player.isAttacking = True
                self.player.attack()
            elif event.type == pygame.MOUSEBUTTONUP:
                self.player.isAttacking = False
                self.player.idle()

    def update(self):
        self.player.update()

    def render(self):
        self.player.draw()
