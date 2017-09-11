import pygame, sys


class ArkanoidGame(object):

    def __init__(self, width=800, height=600):

        # Initialization
        pygame.init()
        self.tps_max = 70.0
        self.screen = pygame.display.set_mode((width, height))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        # Game loop
        while True:

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

    def tick(self):
        pass

    def draw(self):
        pass

if __name__ == "__main__":
    ArkanoidGame()