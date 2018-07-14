__author__ = 'john.young'

import file_util
import json


data = file_util.read_in_json_file("data/example_json.json")

print(data)
