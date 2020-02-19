#!/usr/bin/env python3
from diff.engine import generate_diff, arg_parse
from diff.formatters import recursive, flat


def main():
    file1, file2, form = arg_parse()
    if form == 'json' or form == 'yml':
        print(recursive.rendering(generate_diff(file1, file2, form)))
    elif form == 'plain':
        print(flat.rendering(generate_diff(file1, file2, form)))


if __name__ == '__main__':
    main()
