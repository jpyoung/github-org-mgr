import unittest
import ManagerClasses


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)

    def test_GObject(self):
        go = ManagerClasses.GObject(540, 'Lighthouse')
        self.assertEqual(go.id, 540)
        self.assertEqual(go.name, 'Lighthouse')


if __name__ == '__main__':
    unittest.main()
