import unittest
import file_util
import json
import transformation


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

    def test_repo_read(self):
        keys = [
            "id",
            "name",
            "full_name",
            "git_url",
            "ssh_url",
            "open_issues",
            "clone_url",
            "html_url",
            "pushed_at",
            "org_name",
            "uuid"
        ]
        response_data = file_util.read_in_json_file("../data/example_repo_raw.json")

        data = transformation.include_keys(response_data, keys)

        # check to see if there is a diff between the requested keys and
        # the returned keys. If diff exists, take the delta and insert into
        # dict (defaulting to null)
        diff_keys = transformation.list_diff(keys, data.keys())
        if len(diff_keys) > 0:
            for value in diff_keys:
                data[value] = None

        #print(json.dumps(data, indent=4))
        self.assertEqual(len(data.keys()), 11)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
