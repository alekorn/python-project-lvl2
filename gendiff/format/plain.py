from gendiff.constants import ADDED, DELETED, CHANGED, HAS_CHILDS


def format(dic, out_list=None, path=''):
    if out_list is None:
        out_list = []
    for key, value in dic.items():
        status_key = value['status']
        value_key = value['value']
        if status_key == ADDED:
            if isinstance(value_key, dict):
                new_val = 'complex value'
            else:
                new_val = value_key
            out_list.append(
                    f"Property '{path}{key}' was added with value: '{new_val}'"
                    )
        elif status_key == DELETED:
            out_list.append(f"Property '{path}{key}' was removed")
        elif status_key == CHANGED:
            out_list.append(
                    f"Property '{path}{key}' was changed. "
                    f"From '{value['old_value']}' to '{value_key}'"
                    )
        elif status_key == HAS_CHILDS:
            new_path = path + key + '.'
            format(value_key, out_list, new_path)
    out_list.sort()
    return '\n'.join(out_list).rstrip()
