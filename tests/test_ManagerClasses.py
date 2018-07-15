import unittest
import ManagerClasses


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)

    def test_GObject(self):
        go = ManagerClasses.GObject(1, 'A')
        self.assertEqual(go.id, 1)
        self.assertEqual(go.name, 'A')


if __name__ == '__main__':
    unittest.main()
