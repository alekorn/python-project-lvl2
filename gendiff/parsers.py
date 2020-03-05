from gendiff.loaders import json_load, yaml_load
import os


def parse(file):
    extension = os.path.splitext(file)[1]
    if extension == '.json':
        return json_load(file)
    elif extension == '.yml':
        return yaml_load(file)
    else:
        raise IOError('unsupported file format')
