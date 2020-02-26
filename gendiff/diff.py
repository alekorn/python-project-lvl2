def get_diff(first, second, new_dict=None):
    if new_dict is None:
        new_dict = {}
    if isinstance(first, dict) and isinstance(second, dict):
        deleted, added, not_changed, changed = compare_keys(first, second)
        for key in added:
            new_dict[key] = {'status': 'added', 'value': second[key]}
        for key in deleted:
            new_dict[key] = {'status': 'deleted', 'value': first[key]}
        for key in not_changed:
            new_dict[key] = {'status': 'not_changed', 'value': first[key]}
        for key in changed:
            if isinstance(first[key], dict) and isinstance(second[key], dict):
                new_dict[key] = {'status': 'has_child', 'value': {}}
                get_diff(first[key], second[key], new_dict[key]['value'])
            else:
                new_dict[key] = {
                        'status': 'changed',
                        'value1': first[key],
                        'value2': second[key]
                        }
        return new_dict


def compare_keys(first_dict, second_dict):
    added_keys = (first_dict.keys() - second_dict.keys())
    deleted_keys = (second_dict.keys() - first_dict.keys())
    other_keys = (first_dict.keys() & second_dict.keys())
    not_changed = []
    changed = []
    for key in other_keys:
        if first_dict[key] == second_dict[key]:
            not_changed.append(key)
        else:
            changed.append(key)
    return added_keys, deleted_keys, not_changed, changed
