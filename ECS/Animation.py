import pygame


class Animation(object):
    def __init__(self, sheet, speed=0, flip=False, scale=1):
        self.sheet = sheet
        sheetwidth = sheet.get_width()
        from ECS import Sprite
        self.frame = sheetwidth/(Sprite.SPRITE_WIDTH*scale)
        self.speed = speed/10
        self.flip = flip
        if self.flip:
            self.index = self.frame-1
        else:
            self.index = 0

    def update(self):
        if self.flip:
            if self.index < 0:
                self.index = self.frame-self.speed
            else:
                self.index -= self.speed
        else:
            if self.index > self.frame-self.speed:
                self.index = 0
            else:
                self.index += self.speed
