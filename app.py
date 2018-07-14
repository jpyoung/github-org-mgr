__author__ = 'john.young'

import file_util
import json


data = file_util.read_in_json_file("data/example_json.json")

print(data)

expected_data = {
    "author": "John Young",
    "date": "07-14-2018",
    "repo_name": "github-org-mr"
}

print(expected_data)
print(str(len(data)))
print(data['author'])