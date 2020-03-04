from gendiff.loaders import json_load, yaml_load
import os


# def parse(first_file, second_file):
#     first_ext = os.path.splitext(first_file)[1]
#     second_ext = os.path.splitext(second_file)[1]
#     if first_ext == '.json' and second_ext == '.json':
#         first_dict = json_load(first_file)
#         second_dict = json_load(second_file)
#     elif first_ext == '.yml' and second_ext == '.yml':
#         first_dict = yaml_load(first_file)
#         second_dict = yaml_load(second_file)
#     return first_dict, second_dict

def parse(file):
    extension = os.path.splitext(file)[1]
    if extension == '.json':
        return json_load(file)
    elif extension == '.yml':
        return yaml_load(file)
