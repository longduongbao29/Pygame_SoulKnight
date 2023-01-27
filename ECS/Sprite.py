from ECS import Animation
import pygame

SPRITE_WIDTH = 120
SPRITE_HEIGHT = 80


class Sprite(object):
    def __init__(self, transform, width, height, scale=1):
        self.transform = transform
        self.animations = {}
        self.width = width*scale
        self.height = height*scale
        self.scale = scale
        self.animating = None

    def update(self):
        if self.animating is not None:
            self.animating.update()

    def playAnimation(self, name):
        self.animating = self.animations.get(name)
        if self.animating.frame != 0:
            self.width = self.animating.sheet.get_width()/self.animating.frame
            self.height = self.animating.sheet.get_height()
        else:
            self.width = SPRITE_WIDTH*self.scale
            self.height = SPRITE_HEIGHT*self.scale

    def draw(self):
        from Main import mainScreen
        if self.animating is not None:
            mainScreen.blit(self.animating.sheet, (self.transform.x,
                            self.transform.y), (self.width*int(self.animating.index), 0, self.width, self.height))

    def addSprite(self, name, sheet,  speed, scale=1, flip=False):
        self.animations[name] = Animation.Animation(sheet, speed, flip, scale)
