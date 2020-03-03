ADD = '  + '
DEL = '  - '
TAB = '    '
END = '}'
START = '{'


def rendering(dic, out_list=None, tab=''):
    if out_list is None:
        out_list = []
    else:
        tab += '    '
    for key in dic:
        if dic[key]['status'] == 'added':
            out_list.append(stringify(dic[key]['value'], ADD, key, tab))
        elif dic[key]['status'] == 'deleted':
            out_list.append(stringify(dic[key]['value'], DEL, key, tab))
        elif dic[key]['status'] == 'not_changed':
            out_list.append(stringify(dic[key]['value'], TAB, key, tab))
        elif dic[key]['status'] == 'changed':
            out_list.append(f'{tab}{DEL}{key}: {truefy(dic[key]["old_value"])}')
            out_list.append(f'{tab}{ADD}{key}: {truefy(dic[key]["value"])}')
        elif dic[key]['status'] == 'has_child':
            out_list.append(f'{tab}{TAB}{key}: {START}')
            rendering(dic[key]['value'], out_list, tab)
    if key:
        out_list.append(f'{tab}{END}')
    return '{\n' + '\n'.join(out_list)


def stringify(inp, status, current_key, tab):
    out_string = ''
    if isinstance(inp, dict):
        out_string += f'{tab}{status}{current_key}: {START}\n'
        for key in inp:
            out_string += f'{TAB * 2 + tab}{key}: {truefy(inp[key])}\n'
        out_string += f'{TAB}{tab}{END}'
    else:
        out_string += f'{tab}{status}{current_key}: {truefy(inp)}'
    return out_string


def truefy(string):
    if string is True:
        return 'true'
    if string is None:
        return 'none'
    return string
