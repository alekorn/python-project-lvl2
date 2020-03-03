from gendiff.constants import ADDED, DELETED, NOT_CHANGED, CHANGED, HAS_CHILDS


def get_diff(first, second, new_dict=None):
    if new_dict is None:
        new_dict = {}
    if isinstance(first, dict) and isinstance(second, dict):
        deleted, added, not_changed, changed = compare_keys(first, second)
        for key in added:
            new_dict[key] = {
                    'status': ADDED,
                    'value': second[key]
                    }
        for key in deleted:
            new_dict[key] = {
                    'status': DELETED,
                    'value': first[key]
                    }
        for key in not_changed:
            new_dict[key] = {
                    'status': NOT_CHANGED,
                    'value': first[key]
                    }
        for key in changed:
            first_value = first[key]
            second_value = second[key]
            if (
                    not isinstance(first_value, dict)
                    and
                    not isinstance(second_value, dict)
                    ):
                new_dict[key] = {
                        'status': CHANGED,
                        'old_value': first_value,
                        'value': second_value
                        }
            else:
                inner = {}
                new_dict[key] = {
                        'status': HAS_CHILDS,
                        'value': inner
                        }
                get_diff(first_value, second_value, inner)
        return new_dict


def compare_keys(first_dict, second_dict):
    added_keys = first_dict.keys() - second_dict.keys()
    deleted_keys = second_dict.keys() - first_dict.keys()
    other_keys = first_dict.keys() & second_dict.keys()
    not_changed = []
    changed = []
    for key in other_keys:
        if first_dict[key] == second_dict[key]:
            not_changed.append(key)
        else:
            changed.append(key)
    return added_keys, deleted_keys, not_changed, changed
