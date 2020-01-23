#!/usr/bin/env python3
from diff.formats.json import conv
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
    return args.first_file, args.second_file


def generate_diff(first_file, second_file):
    first, second = conv(first_file, second_file)
    added_keys = first.keys() - second.keys()
    deleted_keys = second.keys() - first.keys()
    other_keys = first.keys() & second.keys()
    print('{')
    for key in other_keys:
        if first[key] == second[key]:
            print(f'    {key}: {first[key]}')
        else:
            print(f'  + {key}: {first[key]}')
            print(f'  - {key}: {second[key]}')
    for key in added_keys:
        print(f'  - {key}: {first[key]}')
    for key in deleted_keys:
        print(f'  + {key}: {second[key]}')
    print('}')
