import pygame
from pygame.math import Vector2

class Ball(object):

    def __init__(self, game):
        self.game = game
        self.resolution = self.game.screen.get_size()
        self.pos = Vector2(self.resolution[0]/2, self.resolution[1]*0.75)
        self.vel = Vector2(3.2, -3.7)
        self.size = {'width':self.resolution[1]/40, 'height':self.resolution[1]/40}

    def tick(self):
        # Add velocity to position
        self.pos += self.vel

        # Check collisions with walls
        if self.pos.x <= 0 or self.pos.x+self.size['width'] >= self.resolution[0]:
            self.vel.x *= -1
        if self.pos.y <= 0 or self.pos.y + self.size['height'] >= self.resolution[1]:
            self.vel.y *= -1

    def draw(self):
        # Rectangle
        rectangle = pygame.Rect(self.pos.x, self.pos.y, self.size['width'], self.size['height'])

        # Drawing oval inside created rectangle
        pygame.draw.ellipse(self.game.screen, (0, 255, 96), rectangle)