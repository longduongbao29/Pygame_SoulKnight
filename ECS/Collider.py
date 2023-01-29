import pygame


TILESET_WIDTH = 18
TILESET_HEIGHT = 11


class Collider(object):
    def __init__(self, xMap, yMap):
        self.xMap = xMap
        self.yMap = yMap

    def update(self):
        pass

    def render(self):
        from Map import TILE_SIZE
        from Main import mainScreen

        pygame.draw.rect(mainScreen, (255, 0, 0), pygame.Rect(
            self.xMap*TILE_SIZE, self.yMap*TILE_SIZE, TILE_SIZE, TILE_SIZE))
        #    mainScreen.blit(self.tileSheet, (self.xMap*TILE_SIZE,
        #  self.yMap*TILE_SIZE), (self.xTileSet*TILE_SIZE, self.yTileSet*TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def getCollider(self):
        from Map import TILE_SIZE
        return pygame.Rect(self.xMap*TILE_SIZE, self.yMap*TILE_SIZE, TILE_SIZE, TILE_SIZE)
