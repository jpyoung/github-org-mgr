__author__ = 'john.young'

import json
import yaml
import csv
#from collections import OrderedDict


def read_in_yaml_file(file_path):
    """
    Read in a YAML configuration file
    :param file_path:
    :return:
    """
    with open(file_path, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
    return cfg


def read_in_csv_file(file_path):
    """
    Read in a CSV file
    :param file_path:
    :return:
    """
    data_list = []
    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            data_list.append(dict(row.copy()))
            line_count += 1
    return data_list


def read_in_file(file_path):
    """

    :rtype : json object
    """
    # Open a file: file
    file = open(file_path, mode='r')

    # read all lines at once
    all_of_it = file.read()

    # close the file
    file.close()
    return all_of_it
    # with open(file_path, 'r') as data_file:
    #     data = data_file
    # return data


def read_in_json_file(file_path):
    """

    :rtype : json object
    """
    with open(file_path) as data_file:
        data = json.load(data_file)
    return data


# def read_in_json_file_keep_order(file_path):
#     """
#
#     :rtype : json object
#     """
#     with open(file_path) as data_file:
#         data = json.load(data_file, object_pairs_hook=OrderedDict)
#
#     return data


def write_json_file(data, outfile):
    with open(outfile, 'w') as f:
        for s in data:
            f.write(s)
    f.close()


# def write_new_package_json(rawData, output_file):
#     """
#
#     :rtype: json object
#     """
#     data = json.dumps(OrderedDict(rawData), indent=2, separators=(",", ": "))
#     with open(output_file, 'w') as f:
#         for s in data:
#             f.write(s)
#     f.close()


