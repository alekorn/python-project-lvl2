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


def generate_diff(first_file, second_file):          # добавить аргумент формат
    first, second = conv(first_file, second_file)    # вынести в скрипт
    added_keys = first.keys() - second.keys()
    deleted_keys = second.keys() - first.keys()
    other_keys = first.keys() & second.keys()
    output_string = '{\n'
    for key in other_keys:
        if first[key] == second[key]:
            output_string += f'    {key}: {first[key]}\n'
        else:
            output_string += f'  + {key}: {first[key]}\n'
            output_string += f'  - {key}: {second[key]}\n'
    for key in added_keys:
        output_string += f'  - {key}: {first[key]}\n'
    for key in deleted_keys:
        output_string += f'  + {key}: {second[key]}\n'
    output_string += '}'
    return output_string
