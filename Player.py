
from ECS import Transform, Sprite

import pygame

KNIGHT_WIDTH = 120*2
KNIGHT_HEIGHT = 80*2
GRAVITY = 1/250
JUMP_TIME = 50
VALOCITY_0 = 2


class Player(object):
    def __init__(self, x=0, y=0):

        self.x = x
        self.y = y
        self.isMoving = False
        self.isAttacking = False
        self.isFalling = True
        self.isJumping = False
        self.isColliding = False

        self.fallingTime = 0
        self.jumpTime = 0
        self.valocity_0 = VALOCITY_0

        self.transform = Transform.Transform(self.x, self.y, 2)
        self.sprite = Sprite.Sprite(
            self.transform, KNIGHT_WIDTH, KNIGHT_HEIGHT)
        self.loadSprite()
        from Game import Direction
        self.direct = Direction.RIGHT
        self.sprite.playAnimation('idle'+self.direct.value)

    def update(self):
        self.transform.setPositionBefore()
        self.idle()

        if self.isColliding:
            self.isFalling = self.isJumping = False
            self.fallingTime = 0
        if not self.onGround():
            self.isFalling = True

        if self.isFalling:
            self.fall()
        if self.isJumping:
            self.jump()

        if self.isAttacking:
            self.attack()
            if self.sprite.animating.animationTime <= 0:
                self.sprite.animating.resetTime()
                self.isAttacking = False
        if self.isMoving:
            self.move()
        self.transform.update()
        self.isColliding = self.checkCollison()
        self.sprite.update()

        if self.isColliding:
            self.transform.resetPosition()

    def draw(self):

        from Main import mainScreen
        pygame.draw.rect(mainScreen, (0, 255, 0), pygame.Rect(
            self.transform.x+75, self.transform.y+75, KNIGHT_WIDTH-175, KNIGHT_HEIGHT-75))
        pygame.draw.circle(mainScreen, (0, 0, 255),
                           (self.transform.x+75+65/2, self.transform.y+160), 10)
        self.sprite.draw()

    def move(self):
        from Game import Direction
        from ECS import Vector
        if self.direct == Direction.LEFT:
            self.transform.valocity.x = -1
        elif self.direct == Direction.RIGHT:
            self.transform.valocity.x = 1
        if not self.isFalling and not self.isJumping:
            self.sprite.playAnimation('run'+self.direct.value)

    def jump(self):
        self.jumpTime += 1
        self.sprite.playAnimation('jump'+self.direct.value)
        self.valocity_0 += GRAVITY*self.jumpTime
        from ECS import Vector
        self.transform.valocity.y = -self.valocity_0
        if self.jumpTime > JUMP_TIME:
            self.isJumping = False
            self.jumpTime = 0
            self.valocity_0 = VALOCITY_0

    def idle(self):
        from ECS import Vector
        self.transform.valocity = Vector.Vector(0, 0)
        self.sprite.playAnimation('idle'+self.direct.value)

    def fall(self):
        self.fallingTime += 1
        self.sprite.playAnimation('fall'+self.direct.value)
        addY = float(1/2*GRAVITY*(self.fallingTime**2))
        from ECS import Vector
        self.transform.valocity.y = addY

    def attack(self):
        self.sprite.playAnimation('attack'+self.direct.value)

    def checkCollison(self):
        from Main import game
        c = game.map.collision
        playerCollider = self.getCollider()
        for col in c:
            tileCollider = col.getCollider()
            if playerCollider.colliderect(tileCollider):
                return True
        return False

    def onGround(self):
        from Map import TILE_SIZE
        from Main import game
        midBottomX = self.transform.x+75+65/2
        midBottomY = self.transform.y+160+10

        mapX = int(midBottomX/TILE_SIZE)
        mapY = int(midBottomY/TILE_SIZE)
        if mapX >= game.map.mapWidth or mapY >= game.map.mapHeight:
            return False
        return int(game.map.mapArray[mapY][mapX]) == 1

    def getCollider(self):
        return pygame.Rect(self.transform.x+75, self.transform.y+75, KNIGHT_WIDTH-175, KNIGHT_HEIGHT-75)

    def loadSprite(self):
        from Game import assetsManager
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

        self.sprite.addSprite(
            'fallRight', assetsManager.spriteManager.sprites.get('knightFall'), 2)

        self.sprite.addSprite('fallLeft', pygame.transform.flip(
            assetsManager.spriteManager.sprites.get('knightFall'), True, False), 2,  True)
        self.sprite.addSprite(
            'jumpRight', assetsManager.spriteManager.sprites.get('knightJump'), 2)

        self.sprite.addSprite('jumpLeft', pygame.transform.flip(
            assetsManager.spriteManager.sprites.get('knightJump'), True, False), 2,  True)
