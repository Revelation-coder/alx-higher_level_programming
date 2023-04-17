import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_size(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

        s2 = Square(10)
        self.assertEqual(s2.size, 10)

    def test_update(self):
        s1 = Square(5)
        s1.update(1, 10)
        self.assertEqual(s1.size, 10)

        s2 = Square(10)
        s2.update(2, 15, 2, 3)
        self.assertEqual(s2.size, 15)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)

    def test_to_dictionary(self):
        s1 = Square(5, 2, 3, 4)
        s1_dict = s1.to_dictionary()
        expected = {'id': 4, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(s1_dict, expected)

        s2 = Square(10)
        s2_dict = s2.to_dictionary()
        expected = {'id': 1, 'size': 10, 'x': 0, 'y': 0}
        self.assertEqual(s2_dict, expected)

if __name__ == '__main__':
    unittest.main()

