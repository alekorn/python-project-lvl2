import json
import yaml


def parse(first_file, second_file, format):
    if format == 'json':
        first_json = json.load(open(first_file))
        second_json = json.load(open(second_file))
        return first_json, second_json
    if format == 'yaml' or format == 'yml':
        first_yaml = yaml.load(open(first_file), Loader=yaml.SafeLoader)
        second_yaml = yaml.load(open(second_file), Loader=yaml.SafeLoader)
        return first_yaml, second_yaml
    if format == 'plain':
        first_json = json.load(open(first_file))
        second_json = json.load(open(second_file))
        return first_json, second_json
