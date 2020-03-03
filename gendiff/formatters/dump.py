import json


def rendering(dictionary):
    return json.dumps(dictionary, indent=4, sort_keys=True)
