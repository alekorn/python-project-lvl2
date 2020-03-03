from gendiff.formatters import recursive, plain, dump
from gendiff.parsers import parse
from gendiff.diff import get_diff
import argparse


def arg_parse():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output'
    )
    parser.add_argument('first_file', help='')
    parser.add_argument('second_file', help='')
    args = parser.parse_args()
    return args


def generate_diff(first_file, second_file, form):
    first, second, files_format = parse(first_file, second_file)
    if form == 'json' and files_format == 'json':
        result = recursive.rendering(get_diff(first, second))
    elif form == 'yaml' and files_format == 'yaml':
        result = recursive.rendering(get_diff(first, second))
    elif form == 'plain':
        result = plain.rendering(get_diff(first, second))
    elif form == 'dump':
        result = dump.rendering(get_diff(first, second))
    return result
