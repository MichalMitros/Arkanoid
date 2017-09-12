import pygame, sys
from paddle import Paddle
from ball import Ball
from brick import Brick


class ArkanoidGame(object):

    def __init__(self, width=800, height=600):
        # Game initialization
        pygame.init()
        pygame.font.init()
        self.tps_max = 100.0
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Arkanoid')
        self.resolution = self.screen.get_size()
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.play = False
        self.is_game_over = False
        self.bricks_rows = 3
        self.bricks_cols = self.bricks_rows + 1
        self.lives = 3

        # Game objects initialization
        self.player = Paddle(self)
        self.ball = Ball(self)
        self.bricks = []

        #Creating bricks (columns, rows)
        self.createBricks(self.bricks_cols, self.bricks_rows)

        # Game loop
        while not self.is_game_over:

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
            self.ball.bounceOffPaddle(self.player)
            for brick in self.bricks:
                if self.ball.isBouncedOffBrick(brick):
                    self.bricks.remove(brick)
            if self.ball.pos.y > self.screen.get_size()[1]:
                if self.lives == 1:
                    self.is_game_over = True
                else:
                    self.lives -= 1
                    self.resetLevel()
            if len(self.bricks) == 0:
                self.nextLevel()

    def draw(self):
        self.ball.draw()
        for brick in self.bricks:
            brick.draw()
        self.player.draw()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('Lives: '+str(self.lives), False, (255, 255, 255))
        self.screen.blit(textsurface, (self.resolution[0]*0.02, self.resolution[1]*0.95))

    def createBricks(self, cols=4, rows=3):
        w = self.screen.get_size()[0]
        h = self.screen.get_size()[1]
        dx = w/cols
        y = 0
        dy = (h/2)/rows
        while y <= h/2-1:
            x = 0
            while x <= w-1:
                self.bricks.append(Brick(self, x+dx/10, y+dy/8, (4*dx)/5, (3*dy)/4))
                x += dx
            y += dy

    def resetLevel(self):
        self.play = False
        self.is_game_over = False

        self.player = Paddle(self)
        self.ball = Ball(self)
        self.bricks = []
        self.createBricks(self.bricks_cols, self.bricks_rows)

    def nextLevel(self):
        self.bricks_rows += 1;
        self.bricks_cols += 1;
        if self.lives != 3:
            self.lives += 1
        self.resetLevel()


# Running game
if __name__ == "__main__":
    while True:
        ArkanoidGame()