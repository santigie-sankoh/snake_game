import random
import sys
import pygame



screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width / gridsize
grid_height = screen_height / gridsize

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)




class Snake:
    """
    This is a class that defines the characteristics and behaviour of our snake.
    """
    def __init__(self):
        self.length = 1
        self.positions = [((screen_width / 2), (screen_height / 2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (17, 24, 47)
        self.score = 0


    def get_head_position(self):
        """
        Method description.
        ###################

        This methods has all the things that needs to happen to our snake when a game reset.
        :return: It returns self.positions[0] when a game reset.
        """
        return self.positions[0]

    def turn(self, point):
        """
        Method description.
        ###################

        This methods has all the things that needs to happen when our snake turns.
        :return: nothing, it just make our snake turn to different direction.
        """
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        """
        Method description.
        ###################

        This methods has all the things that needs to happen when our snake move.
        :return: nothing, it just make our snake move.
        """
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * gridsize)) % screen_width), (cur[1] + (y * gridsize)) % screen_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        """
        Method description.
        ###################

        This methods has all the things that needs to happen  when our game reset.
        :return: nothing, it just reset everything when our game reset.
        """
        self.length = 1
        self.positions = [((screen_width / 2), (screen_height / 2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def draw(self, surface):
        """
        Method description.
        ###################

        This methods has all the things that needs to happen to our game surface.
        :return: nothing, it just draw rectangle on our game surface.
        """
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize, gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)

    def handle_keys(self):
        """
        Method description.
        ###################

        This methods has all the things that needs to happen when our game when user press keys.
        :return: nothing, it just respond to keys user press.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)










