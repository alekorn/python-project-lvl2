import json


def format(dictionary):
    return json.dumps(dictionary, indent=4, sort_keys=True)
