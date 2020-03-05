#!/usr/bin/env python3
from gendiff.engine import arg_parse, get_diff


def main():
    first_dict, second_dict, format = arg_parse()
    print(format(get_diff(first_dict, second_dict)))


if __name__ == '__main__':
    main()
