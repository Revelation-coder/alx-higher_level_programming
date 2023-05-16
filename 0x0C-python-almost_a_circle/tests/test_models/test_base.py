import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_init(self):
        b = Base()
        self.assertEqual(b.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_init_with_id(self):
        b = Base(100)
        self.assertEqual(b.id, 100)

    def test_to_json_string(self):
        b1 = Base(1)
        b2 = Base(2)
        result = Base.to_json_string([b1.to_dictionary(), b2.to_dictionary()])
        expected = '[{"id": 1}, {"id": 2}]'
        self.assertEqual(result, expected)

    def test_from_json_string(self):
        json_str = '[{"id": 1}, {"id": 2}]'
        result = Base.from_json_string(json_str)
        expected = [{'id': 1}, {'id': 2}]
        self.assertEqual(result, expected)

    def test_create(self):
        dictionary = {'id': 100, 'width': 10, 'height': 20, 'x': 30, 'y': 40}
        b = Base.create(**dictionary)
        self.assertIsInstance(b, Base)
        self.assertEqual(b.id, 100)
        self.assertEqual(b.width, 10)
        self.assertEqual(b.height, 20)
        self.assertEqual(b.x, 30)
        self.assertEqual(b.y, 40)

    def test_save_to_file(self):
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        with open("Base.json", "r") as f:
            contents = f.read()
            expected = Base.to_json_string([b1.to_dictionary(), b2.to_dictionary()])
            self.assertEqual(contents, expected)

    def test_load_from_file(self):
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        objs = Base.load_from_file()
        self.assertIsInstance(objs, list)
        self.assertEqual(len(objs), 2)
        self.assertIsInstance(objs[0], Base)
        self.assertIsInstance(objs[1], Base)

    def test_save_to_file_csv(self):
        b1 = Base(1, 10, 20, 30, 40)
        b2 = Base(2, 20, 30, 40, 50)
        Base.save_to_file_csv([b1, b2])
        with open("Base.csv", "r") as f:
            contents = f.read()
            expected = "1,10,20,30,40\n2,20,30,40,50\n"
            self.assertEqual(contents, expected)

    def test_load_from_file_csv(self):
        b1 = Base(1, 10, 20, 30, 40)
        b2 = Base(2, 20, 30, 40, 50)
        Base.save_to_file_csv([b1, b2])
        objs = Base.load_from_file_csv()
        self.assertIsInstance(objs, list)
        self.assertEqual(len(objs), 2)
        self.assertIsInstance(objs[0], Base)
        self.assertIsInstance(objs[1], Base)

if __name__ == '__main__':
    unittest.main()

