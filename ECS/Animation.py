import pygame


class Animation(object):
    def __init__(self, sheet, spite, speed=0, flip=False):
        self.sheet = sheet
        sheetwidth = sheet.get_width()
        self.frame = sheetwidth/(spite.width)
        self.speed = speed/10
        self.flip = flip
        if self.flip:
            self.index = self.frame-1
        else:
            self.index = 0
        self.animationTime = self.frame/self.speed

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
        self.animationTime -= 1

    def resetTime(self):
        self.animationTime = self.frame/self.speed
