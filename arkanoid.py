import pygame, sys
from paddle import Paddle
from ball import Ball


class ArkanoidGame(object):

    def __init__(self, width=800, height=600):
        # Game initialization
        pygame.init()
        self.tps_max = 100.0
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Arkanoid')
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.play = False

        # Game objects initialization
        self.player = Paddle(self)
        self.ball = Ball(self)

        # Game loop
        while True:

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and not event.key == pygame.K_ESCAPE:
                    self.play = True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            # Rendering
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

    def tick(self):
        if self.play:
            self.player.tick()
            self.ball.tick()

    def draw(self):
        self.ball.draw()
        self.player.draw()


# Running game
if __name__ == "__main__":
    ArkanoidGame()