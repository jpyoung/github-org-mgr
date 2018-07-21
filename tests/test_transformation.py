import unittest
import transformation


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)

    def test_include_keys(self):
        data = {
            "a": "aa",
            "b": "bb",
            "c": "cc",
            "d": "dd",
            "f": {
                "g": "gg",
                "h": "hh"
            }
        }
        result = transformation.include_keys(data, ["a", "b"])
        self.assertDictEqual(result, {'a': 'aa', 'b': 'bb'})

    def test_exclude_keys(self):
        data = {
            "a": "aa",
            "b": "bb",
            "c": "cc",
            "d": "dd"
        }
        result = transformation.exclude_keys(data, ["c", "a"])
        self.assertDictEqual(result, {'b': 'bb', 'd': 'dd'})

    def test_list_diff(self):
        data = {
            "a": "aa",
            "b": "bb",
            "c": "cc",
            "d": "dd"
        }
        keys = ["a", "b", "c", "g", "f"]
        diff_keys = transformation.list_diff(keys, data.keys())
        self.assertIn(diff_keys[0], ['f', 'g'])
        self.assertIn(diff_keys[1], ['f', 'g'])
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
