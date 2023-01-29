
from ECS import Transform, Sprite

import pygame

KNIGHT_WIDTH = 120
KNIGHT_HEIGHT = 80


class Player(object):
    def __init__(self, x=0, y=0):
        from Game import assetsManager
        self.x = x
        self.y = y
        self.isMoving = False
        self.isAttacking = False
        self.transform = Transform.Transform(self.x, self.y, 2)
        self.sprite = Sprite.Sprite(
            self.transform, KNIGHT_WIDTH, KNIGHT_HEIGHT)

        self.sprite.addSprite(
            'idleRight', assetsManager.spriteManager.sprites.get('knightIdle'), 2)

        self.sprite.addSprite(
            'idleLeft', pygame.transform.flip(assetsManager.spriteManager.sprites.get('knightIdle'), True, False), 2, True)

        self.sprite.addSprite('runLeft', pygame.transform.flip(
            assetsManager.spriteManager.sprites.get('knightRun'), True, False), 2,  True)

        self.sprite.addSprite(
            'runRight', assetsManager.spriteManager.sprites.get('knightRun'), 2)

        self.sprite.addSprite('attackLeft', pygame.transform.flip(
            assetsManager.spriteManager.sprites.get('knightAttack'), True, False), 2,  True)

        self.sprite.addSprite(
            'attackRight', assetsManager.spriteManager.sprites.get('knightAttack'), 2)

        from Game import Direction
        self.direct = Direction.RIGHT
        self.sprite.playAnimation('idle'+self.direct.value)

    def update(self):
        self.transform.update()
        self.sprite.update()
        if self.isMoving:
            self.move()
        elif self.isAttacking:
            self.attack()
        else:
            self.idle()
        if self.sprite.animating.animationTime <= 0:
            self.sprite.animating.resetTime()
            self.isAttacking = False

    def draw(self):
        self.sprite.draw()

    def move(self):
        from Game import Direction
        from ECS import Vector
        if self.direct == Direction.LEFT:
            self.transform.valocity = Vector.Vector(-1, 0)
        elif self.direct == Direction.RIGHT:
            self.transform.valocity = Vector.Vector(1, 0)

        self.sprite.playAnimation('run'+self.direct.value)

    def idle(self):
        from ECS import Vector
        self.transform.valocity = Vector.Vector(0, 0)
        self.sprite.playAnimation('idle'+self.direct.value)

    def attack(self):
        self.sprite.playAnimation('attack'+self.direct.value)
