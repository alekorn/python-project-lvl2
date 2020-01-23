import json


def conv(first_file, second_file):
    first_json = json.load(open(first_file))
    second_json = json.load(open(second_file))
    return first_json, second_json
