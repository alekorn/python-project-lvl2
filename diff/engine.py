from diff.parsers import parse
import argparse

ADD = '  + '
DEL = '  - '
TAB = '    '
END = '}'
START = '{'


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
    return args.first_file, args.second_file, args.format


def generate_diff(first_file, second_file, format):
    first, second = parse(first_file, second_file, format)  # в скрипт
    return get_diff(first, second)


def get_diff(first, second, new_dict=None):
    if new_dict is None:
        new_dict = {}
    if isinstance(first, dict) and isinstance(second, dict):
        deleted, added, not_changed, changed = compare_keys(first, second)
        for key in added:
            new_dict[('added', key)] = second[key]
        for key in deleted:
            new_dict[('deleted', key)] = first[key]
        for key in not_changed:
            new_dict[('not_changed', key)] = first[key]
        for key in changed:
            if not isinstance(first[key], dict) and not isinstance(second[key], dict):
                new_dict[('changed', key)] = (first[key], second[key])
            else:
                new_dict[('has_child', key)] = {}
                get_diff(
                    first[key],
                    second[key],
                    new_dict[('has_child', key)]
                )
        return new_dict


def compare_keys(first_dict, second_dict):
    added_keys = sorted(first_dict.keys() - second_dict.keys())
    deleted_keys = sorted(second_dict.keys() - first_dict.keys())
    other_keys = sorted(first_dict.keys() & second_dict.keys())
    not_changed = []
    changed = []
    for key in other_keys:
        if first_dict[key] == second_dict[key]:
            not_changed.append(key)
        else:
            changed.append(key)
    return added_keys, deleted_keys, not_changed, changed


def rendering(new_dict, new_list=None, tab=''):
    if new_list is None:
        new_list = []
    if new_list:
        tab += '    '
    for key in new_dict:
        if key[0] == 'has_child' and key[1]:
            new_list.append(f'{tab}{TAB}{key[1]}: {START}')
        if key[0] == 'has_child':
            rendering(new_dict[key], new_list, tab)
    for key in new_dict:
        if key[0] == 'added' and isinstance(new_dict[key], dict):
            new_list.append(f'{tab}{ADD}{key[1]}: {START}')
            new_list.append(f'{TAB * 2 + tab}{stringify(new_dict[key])}')
            new_list.append(f'{TAB}{tab}{END}')
        elif key[0] == 'added':
            new_list.append(f'{tab}{ADD}{key[1]}: {new_dict[key]}')
        if key[0] == 'deleted' and isinstance(new_dict[key], dict):
            new_list.append(f'{tab}{DEL}{key[1]}: {START}')
            new_list.append(f'{TAB * 2 + tab}{stringify(new_dict[key])}')
            new_list.append(f'{TAB}{tab}{END}')
        elif key[0] == 'deleted':
            new_list.append(f'{tab}{DEL}{key[1]}: {new_dict[key]}')
        if key[0] == 'not_changed' and isinstance(new_dict[key], dict):
            new_list.append(f'{tab}{TAB}{key[1]}: {START}')
            new_list.append(f'{TAB * 2 + tab}{stringify(new_dict[key])}')
            new_list.append(f'{TAB}{tab}{END}')
        elif key[0] == 'not_changed':
            new_list.append(f'{tab}{TAB}{key[1]}: {new_dict[key]}')
        if key[0] == 'changed' and isinstance(new_dict[key], dict):
            new_list.append(f'{tab}{TAB}{key[1]}: {START}')
            new_list.append(f'{tab}{DEL}{key[1]}: {new_dict[key][0]}')
            new_list.append(f'{tab}{ADD}{key[1]}: {new_dict[key][1]}')
            new_list.append(f'{TAB}{tab}{END}')
        elif key[0] == 'changed':
            new_list.append(f'{tab}{DEL}{key[1]}: {new_dict[key][0]}')
            new_list.append(f'{tab}{ADD}{key[1]}: {new_dict[key][1]}')
    if key[1]:
        new_list.append(f'{tab}{END}')
    return '{\n' + '\n'.join(new_list)


def stringify(new_dict):
    out_string = ''
    for key in new_dict:
        out_string += f'{key}: {new_dict[key]}'
    return (out_string)
