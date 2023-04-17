import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_init(self):
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(5, 5, 10, 10, 100)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 10)
        self.assertEqual(r2.y, 10)
        self.assertEqual(r2.id, 100)

    def test_area(self):
        r1 = Rectangle(5, 10)
        self.assertEqual(r1.area(), 50)

        r2 = Rectangle(3, 7, 2, 1, 10)
        self.assertEqual(r2.area(), 21)

    def test_display(self):
        r1 = Rectangle(3, 2)
        r1.display()

        r2 = Rectangle(2, 3)
        r2.display()

        r3 = Rectangle(1, 1, 1, 1)
        r3.display()

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update(2)
        self.assertEqual(str(r1), "[Rectangle] (2) 10/10 - 10/10")
        r1.update(3, 5)
        self.assertEqual(str(r1), "[Rectangle] (3) 10/10 - 5/10")
        r1.update(4, 6, 7)
        self.assertEqual(str(r1), "[Rectangle] (4) 7/10 - 6/10")
        r1.update(5, 8, 9, 10)
        self.assertEqual(str(r1), "[Rectangle] (5) 9/10 - 8/10")

if __name__ == '__main__':
    unittest.main()
