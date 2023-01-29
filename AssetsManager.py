import pygame


class Sprite(object):
    def __init__(self):
        self.sprites = {}

    def addSprite(self, name, path, scale):
        sprite = pygame.image.load(path)
        width = sprite.get_width()
        height = sprite.get_height()
        spriteScale = pygame.transform.scale(
            sprite, (width*scale, height*scale))
        self.sprites[name] = spriteScale


class Sound(object):
    pass


class AssetsManager(object):
    def __init__(self):
        self.spriteManager = Sprite()
        self.spriteManager.addSprite(
            'knightIdle', 'assets/FreeKnight_v1/Colour2/Outline/120x80_PNGSheets/_Idle.png', 2)
        self.spriteManager.addSprite(
            'knightRun', 'assets/FreeKnight_v1/Colour2/Outline/120x80_PNGSheets/_Run.png', 2)
        self.spriteManager.addSprite(
            'knightAttack', 'assets/FreeKnight_v1/Colour2/Outline/120x80_PNGSheets/_Attack2.png', 2)
        self.spriteManager.addSprite(
            'knightFall', 'assets/FreeKnight_v1/Colour2/Outline/120x80_PNGSheets/_Fall.png', 2)
        self.spriteManager.addSprite(
            'knightJump', 'assets/FreeKnight_v1/Colour2/Outline/120x80_PNGSheets/_Jump.png', 2)

        self.tileset = pygame.transform.scale2x(
            pygame.image.load("assets/map/tileset.png"))
