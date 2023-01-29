import pygame
from enum import Enum
from AssetsManager import AssetsManager
from Player import Player
from Map import Map


assetsManager = AssetsManager()


class Direction(Enum):
    LEFT = 'Left'
    RIGHT = 'Right'


class Game(object):
    def __init__(self):
        self.running = True

        self.level = 1
        self.map = Map()
        self.map.load(self.level)

        self.player = Player(300, 0)

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
                elif event.key == pygame.K_SPACE:
                    self.player.isJumping = True
            elif event.type == pygame.KEYUP:
                self.player.isMoving = False
                self.player.idle()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.player.isAttacking = True
                self.player.attack()

    def update(self):
        self.player.update()

    def render(self):
        self.map.render()
        self.player.draw()
