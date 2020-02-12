ADD = '  + '
DEL = '  - '
TAB = '    '
END = '}'
START = '{'


def rendering(new_dict, new_list=None, tab=''):
    if new_list is None:
        new_list = []
    else:
        tab += '    '
    for key in new_dict:
        if key[0] == 'has_child' and key[1]:
            new_list.append(f'{tab}{TAB}{key[1]}: {START}')
        if key[0] == 'has_child':
            rendering(new_dict[key], new_list, tab)
    for key in new_dict:
        if key[0] == 'added' and isinstance(new_dict[key], dict):
            new_list.append(f'{tab}{ADD}{key[1]}: {START}')
            new_list.append(f'{stringify(new_dict[key], tab)}')
            new_list.append(f'{TAB}{tab}{END}')
        elif key[0] == 'added':
            new_list.append(f'{tab}{ADD}{key[1]}: {truefy(new_dict[key])}')
        if key[0] == 'deleted' and isinstance(new_dict[key], dict):
            new_list.append(f'{tab}{DEL}{key[1]}: {START}')
            new_list.append(f'{stringify(new_dict[key], tab)}')
            new_list.append(f'{TAB}{tab}{END}')
        elif key[0] == 'deleted':
            new_list.append(f'{tab}{DEL}{key[1]}: {truefy(new_dict[key])}')
        if key[0] == 'not_changed' and isinstance(new_dict[key], dict):
            new_list.append(f'{tab}{TAB}{key[1]}: {START}')
            new_list.append(f'{stringify(new_dict[key], tab)}')
            new_list.append(f'{TAB}{tab}{END}')
        elif key[0] == 'not_changed':
            new_list.append(f'{tab}{TAB}{key[1]}: {truefy(new_dict[key])}')
        if key[0] == 'changed' and isinstance(new_dict[key], dict):
            new_list.append(f'{tab}{TAB}{key[1]}: {START}')
            new_list.append(f'{tab}{DEL}{key[1]}: {truefy(new_dict[key][0])}')
            new_list.append(f'{tab}{ADD}{key[1]}: {truefy(new_dict[key][1])}')
            new_list.append(f'{TAB}{tab}{END}')
        elif key[0] == 'changed':
            new_list.append(f'{tab}{DEL}{key[1]}: {truefy(new_dict[key][0])}')
            new_list.append(f'{tab}{ADD}{key[1]}: {truefy(new_dict[key][1])}')
    if key[1]:
        new_list.append(f'{tab}{END}')
    return '{\n' + '\n'.join(new_list)


def stringify(new_dict, tab):
    out_string = ''
    for key in new_dict:
        out_string += f'{TAB * 2 + tab}{key}: {truefy(new_dict[key])}\n'
    return out_string.rstrip()


def truefy(string):
    if string is True:
        return 'true'
    if string is None:
        return 'none'
    return string
