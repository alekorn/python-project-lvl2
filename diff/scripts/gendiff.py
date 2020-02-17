#!/usr/bin/env python3
from diff.engine import generate_diff, arg_parse
from diff.formatters import json_format


def main():
    first_file, second_file, format = arg_parse()
    print(json_format.rendering(generate_diff(first_file, second_file, format)))


if __name__ == '__main__':
    main()
