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
        data = file_util.read_in_json_file("data/4312example_json.json")
        print(data)
        expected_data = {
            "author": "John Young",
            "date": "07-14-2018",
            "repo_name": "github-org-mr"
        }
        self.assertEqual(data, expected_data)

    def test_read_in_json_file(self):
        data = file_util.read_in_json_file("data/example_json.json")
        expected_data = {
            "author": "John Young",
            "date": "07-14-2018",
            "repo_name": "github-org-mgr"
        }

if __name__ == '__main__':
    unittest.main()
