#!/usr/bin/env python3
from diff.engine import generate_diff, arg_parse, rendering


def main():
    first_file, second_file, format = arg_parse()
    print(rendering(generate_diff(first_file, second_file, format)))


if __name__ == '__main__':
    main()
