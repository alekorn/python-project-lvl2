def rendering(dic, out_list=None, path=''):
    if out_list is None:
        out_list = []
    for key, value in dic.items():
        status_key = value['status']
        value_key = value['value']
        if status_key == 'added':
            if isinstance(value_key, dict):
                new_val = 'complex value'
            else:
                new_val = value_key
            out_list.append(
                    f"Property '{path}{key}' was added with value: '{new_val}'"
                    )
        elif status_key == 'deleted':
            out_list.append(f"Property '{path}{key}' was removed")
        elif status_key == 'changed':
            out_list.append(
                    f"Property '{path}{key}' was changed. "
                    f"From '{value['old_value']}' to '{value_key}'"
                    )
        elif status_key == 'has_child':
            new_path = path + key + '.'
            rendering(value_key, out_list, new_path)
    out_list.sort()
    return '\n'.join(out_list).rstrip()
