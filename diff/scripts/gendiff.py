#!/usr/bin/env python3
from diff.engine import generate_diff, arg_parse
import argparse


def main():
    first_file, second_file = arg_parse()
    generate_diff(first_file, second_file)


if __name__ == '__main__':
    main()
