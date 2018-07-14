import unittest
import file_util


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)

    def test_comp_strings(self):
        x = "Jack"
        y = "Jack"
        self.assertEqual(x, y)

    def test_read_in_json_file(self):
        data = file_util.read_in_json_file("../data/example_json.json")
        print(data)
        print("jack")
        expected_data = {
            "author": "John Young",
            "date": "07-14-2018",
            "repo_name": "github-org-mgr"
        }
        self.assertDictEqual(data, expected_data)
        self.assertEqual(data['author'], expected_data['author'])
        self.assertEqual(data['date'], expected_data['date'])
        self.assertEqual(data['repo_name'], expected_data['repo_name'])
        self.assertEqual(len(data), 3)


if __name__ == '__main__':
    unittest.main()
