from ECS import Animation
import pygame


class Sprite(object):
    def __init__(self, transform, width, height):
        self.transform = transform
        self.animations = {}
        self.width = width
        self.height = height
        self.animating = None

    def update(self):
        if self.animating is not None:
            self.animating.update()

    def playAnimation(self, name):
        self.animating = self.animations.get(name)

    def draw(self):
        from Main import mainScreen
        if self.animating is not None:
            mainScreen.blit(self.animating.sheet, (self.transform.x,
                            self.transform.y), (self.width*int(self.animating.index), 0, self.width, self.height))

    def addSprite(self, name, sheet,  speed,  flip=False):
        self.animations[name] = Animation.Animation(sheet, self, speed, flip)
