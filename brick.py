import pygame
from pygame.math import Vector2


class Brick(object):

    def __init__(self, game, x, y, width, height):
        self.game = game
        self.resolution = self.game.screen.get_size()
        self.size = {'width':width, 'height':height}
        self.pos = Vector2(x, y)

    def tick(self):
        pass

    def draw(self):
        # Rectangle
        rectangle = pygame.Rect(self.pos.x, self.pos.y, self.size['width'], self.size['height'])

        # Drawing ractangle
        pygame.draw.rect(self.game.screen, (255, 96, 96), rectangle)