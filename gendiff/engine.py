from gendiff import format
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


def generate_diff(first_file, second_file, name):
    first = parse(first_file)
    second = parse(second_file)
    if name == format.JSON:
        return format.json(get_diff(first, second))
    elif name == format.PLAIN:
        return format.plain(get_diff(first, second))
    elif name == format.DEFAULT:
        return format.default(get_diff(first, second))
#    if form == 'json' and files_format == 'json':
#        result = recursive.rendering(get_diff(first, second))
#    elif form == 'yaml' and files_format == 'yaml':
#        result = recursive.rendering(get_diff(first, second))
#    elif form == 'plain':
#        result = plain.rendering(get_diff(first, second))
#    elif form == 'dump':
#        result = dump.rendering(get_diff(first, second))
#    return result
