from gendiff import format
from gendiff.parsers import parse
from gendiff.diff import get_diff
import argparse


def arg_parse():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output',
        type=format_choise,
        default='default'
    )
    parser.add_argument('first_file', type=parse, help='')
    parser.add_argument('second_file', type=parse, help='')
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format


def generate_diff(first_file, second_file, name='default'):
    first = parse(first_file)
    second = parse(second_file)
    return format_choise(name)(get_diff(first, second))


def format_choise(name):
    if name == format.JSON:
        return format.json
    elif name == format.PLAIN:
        return format.plain
    elif name == format.DEFAULT:
        return format.default
