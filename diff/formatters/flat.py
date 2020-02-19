def rendering(dic, out_list=None, path=''):
    if out_list is None:
        out_list = []
    for key in dic:
        if dic[key]['status'] == 'added':
            if isinstance(dic[key]['value'], dict):
                value = 'complex value'
            else:
                value = dic[key]['value']
            out_list.append(
                    f"Property '{path}{key}' was added with value: '{value}'"
                    )
        elif dic[key]['status'] == 'deleted':
            out_list.append(f"Property '{path}{key}' was removed")
        elif dic[key]['status'] == 'changed':
            out_list.append(
                    f"Property '{path}{key}' was changed. "
                    f"From '{dic[key]['value1']}' to '{dic[key]['value2']}'"
                    )
        elif dic[key]['status'] == 'has_child':
            new_path = path + key + '.'
            rendering(dic[key]['value'], out_list, new_path)
    return '\n'.join(out_list).rstrip()
