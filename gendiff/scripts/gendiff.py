#!/usr/bin/env python3
from gendiff.engine import arg_parse, generate_diff


def main():
    file1, file2, form = arg_parse()
    print(generate_diff(file1, file2, form))


if __name__ == '__main__':
    main()
