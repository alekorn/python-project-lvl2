from gendiff.constants import ADDED, DELETED, CHANGED, NOT_CHANGED, HAS_CHILDS
ADD = '  + '
DEL = '  - '
TAB = '    '
END = '}'
START = '{'


def rendering(dic, out_list=None, tab=''):
    if out_list is None:
        out_list = [START]
    else:
        tab += '    '
    for key, value in dic.items():
        status_key = value['status']
        value_key = value['value']
        if status_key == ADDED:
            out_list.extend(stringify(value_key, ADD, key, tab))
        elif status_key == DELETED:
            out_list.extend(stringify(value_key, DEL, key, tab))
        elif status_key == NOT_CHANGED:
            out_list.extend(stringify(value_key, TAB, key, tab))
        elif status_key == CHANGED:
            out_list.append(f'{tab}{DEL}{key}: {truefy(value["old_value"])}')
            out_list.append(f'{tab}{ADD}{key}: {truefy(value_key)}')
        elif status_key == HAS_CHILDS:
            out_list.append(f'{tab}{TAB}{key}: {START}')
            rendering(value_key, out_list, tab)
    if key:
        out_list.append(f'{tab}{END}')
    return '\n'.join(out_list)


def stringify(inp, status, current_key, tab):
    out_list = []
    if isinstance(inp, dict):
        out_list.append(f'{tab}{status}{current_key}: {START}')
        for key in inp:
            out_list.append(f'{TAB * 2 + tab}{key}: {truefy(inp[key])}')
        out_list.append(f'{TAB}{tab}{END}')
    else:
        out_list.append(f'{tab}{status}{current_key}: {truefy(inp)}')
    return out_list


def truefy(string):
    if string is True:
        return 'true'
    if string is None:
        return 'none'
    return string
