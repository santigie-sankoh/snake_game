import pygame
import random

from Snake_class import *



class Food(Snake):
    """
    This is a class that defines the characteristics and behaviour of our snake's food.
    """
    def __init__(self, position, color, randomize):
        super().__init__()
        self.position = (0, 0)
        self.color = (223, 163, 49)
        self.randomize_position()


    def randomize_position(self):
        """
        Method description.
        ###################

        This methods has all the things that needs to our food.
        :return: nothing, it just place our food in random position whenever our game reset.
        """
        self.position = (random.randint(0, grid_width - 1) * gridsize, random.randint(0, grid_height - 1) * gridsize)


    def draw(self, surface):
        """
        Method description.
        ###################

        This methods has all the things that needs to happen to our food.
        :return: nothing, it just draws our food and give it attributes.
        """
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)



def drawGrid(surface):
    """
    Method description.
    ###################

    This methods has all the things that needs to happen to our game surface.
    :return: nothing, it just draw exact rectangle on our game surface.
    """
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, (93, 216, 228), r)
            else:
                rr = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, (84, 194, 205), rr)

