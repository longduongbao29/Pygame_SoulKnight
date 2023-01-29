from ECS import Vector


class Transform(object):
    def __init__(self, x, y, speed=1):
        self.x = float(x)
        self.y = float(y)
        self.valocity = Vector.Vector(0, 0)
        self.speed = speed

    def update(self):
        self.x += self.valocity.x*self.speed
        self.y += self.valocity.y

    def add(self, x, y):
        self.x += x
        self.y += y

    def resetPosition(self):
        self.x = self.beforeX
        self.y = self.beforeY

    def setPositionBefore(self):
        self.beforeX = self.x
        self.beforeY = self.y
