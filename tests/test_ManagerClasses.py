import unittest
import ManagerClasses


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)

    def test_GObject(self):
        go = ManagerClasses.GObject(1, 'A')
        self.assertEqual(go.id, 1)
        self.assertEqual(go.name, 'A')

    def test_label_class(self):
        label_data_v1 = {
            "id": 1,
            "name": "bug",
            "color": "d73a4a"
        }
        label = ManagerClasses.Label(1, "bug", "d73a4a")
        self.assertDictEqual(label.toJSON(), label_data_v1)

    def test_object_keys_label(self):
        expected_keys = [
            'color',
            'id',
            'name'
        ]
        label = ManagerClasses.Label(1, "bug", "d73a4a")
        self.assertListEqual(label.obj_keys(), expected_keys)

    def test_object_keys_repo(self):
        expected_keys = [
            'org_name',
            'name',
            'html_url',
            'pushed_at',
            'clone_url',
            'git_url',
            'ssh_url',
            'open_issues',
            'id'
        ]
        repo = ManagerClasses.Repo(1, "A")
        self.assertListEqual(repo.obj_keys(), expected_keys)

    def test_comp_org(self):
        org1 = ManagerClasses.Org(1, 'AA', 'http://github.com/AA')
        self.assertEqual(org1.id, 1)
        self.assertEqual(org1.name, 'AA')
        self.assertEqual(org1.avatar_url, 'http://github.com/AA')

    def test_comp_ORGS(self):
        org1 = ManagerClasses.Org(1, 'AA', 'http://github.com/AA')
        org2 = ManagerClasses.Org(2, 'BB', 'http://github.com/BB')

        orgs = ManagerClasses.Orgs()

        # orgs is an empty list
        self.assertListEqual(orgs.list(), [])

        # checking orgs.list returns one org
        orgs.add_org(org1)
        self.assertListEqual(orgs.list(), [org1.toJSON()])

        orgs.add_org(org2)
        self.assertListEqual(orgs.list(), [org1.toJSON(), org2.toJSON()])


if __name__ == '__main__':
    unittest.main()
