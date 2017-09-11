import pygame
from pygame.math import Vector2

class Paddle(object):

    def __init__(self, game):
        self.game = game
        self.resolution = self.game.screen.get_size()
        self.pos = Vector2(self.resolution[0]/2, self.resolution[1]*0.9)
        self.size = {'width':self.resolution[0]/5, 'height':self.resolution[1]/80}
        self.speed = 4

    def tick(self):
        # Input check
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_RIGHT] and self.pos.x+self.size['width'] <= self.resolution[0]:
            self.pos.x += self.speed
        elif pressed[pygame.K_LEFT] and self.pos.x >= 0:
            self.pos.x -= self.speed

    def draw(self):
        # Rectangle
        rectangle = pygame.Rect(self.pos.x, self.pos.y, self.size['width'], self.size['height'])

        # Drawing ractangle
        pygame.draw.rect(self.game.screen, (0, 96, 255), rectangle)