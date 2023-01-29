import pygame
from ECS.Collider import Collider

TILE_SIZE = 32


class Map(object):
    def __init__(self):
        self.mapWidth = None
        self.mapHeight = None
        self.mapArray = None
        self.map = None
        self.collision = []

    def load(self, level):
        self.map = pygame.image.load("assets/map/map{}.png".format(level))
        self.map = pygame.transform.scale2x(self.map)
        f = open("assets/map/map{}.map".format(level), 'r')
        self.mapWidth = int(f.readline())
        self.mapHeight = int(f.readline())
        self.mapArray = [[0]*self.mapWidth]*self.mapHeight
        for i in range(self.mapHeight):
            self.mapArray[i] = f.readline().split()
        for i in range(self.mapHeight):
            for j in range(self.mapWidth):
                if int(self.mapArray[i][j]) == 1:
                    self.collision.append(Collider(j, i))
        f.close()

    def update(self):
        pass

    def render(self):
        from Main import mainScreen
        mainScreen.blit(self.map, (0, 0))
        for c in self.collision:
            c.render()
