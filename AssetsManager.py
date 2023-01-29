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
            'knightIdle', 'assets/FreeKnight_v1/Colour2/Outline/120x80_PNGSheets/_Idle.png', 1)
        self.spriteManager.addSprite(
            'knightRun', 'assets/FreeKnight_v1/Colour2/Outline/120x80_PNGSheets/_Run.png', 1)
        self.spriteManager.addSprite(
            'knightAttack', 'assets/FreeKnight_v1/Colour2/Outline/120x80_PNGSheets/_Attack2.png', 1)
