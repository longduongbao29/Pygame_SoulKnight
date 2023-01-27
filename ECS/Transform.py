from ECS import Vector


class Transform(object):
    def __init__(self, x, y, speed=1):
        self.x = x
        self.y = y
        self.valocity = Vector.Vector(0, 0)
        self.speed = speed

    def update(self):
        self.x += self.valocity.x*self.speed
        self.y += self.valocity.y
