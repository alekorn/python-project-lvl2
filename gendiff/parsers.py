import json
import yaml
import os


def parse(first_file, second_file):
    first_ext = os.path.splitext(first_file)[1]
    second_ext = os.path.splitext(second_file)[1]
    if first_ext == '.json' and second_ext == '.json':
        files_format = 'json'
        first_dict = json.load(open(first_file))
        second_dict = json.load(open(second_file))
    elif first_ext == '.yml' and second_ext == '.yml':
        files_format = 'yaml'
        first_dict = yaml.load(open(first_file), Loader=yaml.SafeLoader)
        second_dict = yaml.load(open(second_file), Loader=yaml.SafeLoader)
    return first_dict, second_dict, files_format
