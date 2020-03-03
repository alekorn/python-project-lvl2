#!/usr/bin/env python3
from gendiff.engine import arg_parse, generate_diff


def main():
    print(generate_diff(
        arg_parse().first_file,
        arg_parse().second_file,
        arg_parse().format))


if __name__ == '__main__':
    main()
