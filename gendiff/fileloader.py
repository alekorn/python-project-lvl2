import json
import yaml


def json_load(file):
    with open(file, "r") as read_file:
        data = json.load(read_file)
    return data


def yaml_load(file):
    with open(file, "r") as read_file:
        data = yaml.safe_load(read_file)
    return data


def txt_load(file):
    with open(file, "r") as read_file:
        data = read_file.read().rstrip()
    return data
