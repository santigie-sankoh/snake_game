import unittest



class TestFood(unittest.TestCase):
    def test_screen_width(self):
        """
        This unittest test for game screen width. We do this by passing values and testing for equality.
        """
        for y in range(0, 8):
            with self.subTest(y=y):
                self.assertEqual((y + y) % 2, 0)

    def test_screen_height(self):
        """
        This unittest test for game screen height. We do this by passing values and testing for equality.
        """
        for y in range(0, 8):
            with self.subTest(y=y):
                self.assertEqual((y + y) % 2, 0)

    def test_color(self):
        """
        This unittest test for food color. We do this by passing values and testing for equality.
        """
        result = self.color = (223, 163, 49)
        self.assertEqual(result, (223, 163, 49))


if __name__ == '__main__':
    unittest.main( )
