import unittest
import Snake_class

positions = []


def get_head_position():
    pass


class Test_snake(unittest.TestCase):

    def test_exit(self):
        self.assertEqual('exit'.upper( ), 'EXIT')

    def test_handle_keys(self):
        from pygame.examples.prevent_display_stretching import event
        import pygame
        self.assertIs(event.key, pygame.K_DOWN)

    def test_reset(self):
        snake_position = 0
        self.assertIs(snake_position, 0)

    def test_move(self):
        positions.pop()
        self.assertIn(get_head_position(), positions.pop())

    def test_draw(self):
        self.assertEqual([0, 1, 2, 3], [0, 1, 2, 3])


if __name__ == '__main__':
    unittest.main( )
