from diff.parsers import parse
import argparse


def arg_parse():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output'
    )
    parser.add_argument('first_file', type=str, help='')
    parser.add_argument('second_file', type=str, help='')
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format


def generate_diff(first_file, second_file, format):
    first, second = parse(first_file, second_file, format)
    return get_diff(first, second)


def get_diff(first, second, new_dict=None):
    if new_dict is None:
        new_dict = {}
    if isinstance(first, dict) and isinstance(second, dict):
        deleted, added, not_changed, changed = compare_keys(first, second)
        for key in added:
            new_dict[('added', key)] = second[key]
        for key in deleted:
            new_dict[('deleted', key)] = first[key]
        for key in not_changed:
            new_dict[('not_changed', key)] = first[key]
        for key in changed:
            if isinstance(first[key], dict) and isinstance(second[key], dict):
                new_dict[('has_child', key)] = {}
                get_diff(
                    first[key],
                    second[key],
                    new_dict[('has_child', key)]
                )
            else:
                new_dict[('changed', key)] = (first[key], second[key])
        return new_dict


def compare_keys(first_dict, second_dict):
    added_keys = (first_dict.keys() - second_dict.keys())
    deleted_keys = (second_dict.keys() - first_dict.keys())
    other_keys = (first_dict.keys() & second_dict.keys())
    not_changed = []
    changed = []
    for key in other_keys:
        if first_dict[key] == second_dict[key]:
            not_changed.append(key)
        else:
            changed.append(key)
    return added_keys, deleted_keys, not_changed, changed
