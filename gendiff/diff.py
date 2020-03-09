from gendiff.constants import (
        ADDED, DELETED, NOT_CHANGED, CHANGED,
        HAS_CHILDS, STATUS, VALUE, OLD_VALUE
        )


def get_diff(first, second, new_dict=None):
    if new_dict is None:
        new_dict = {}
    if isinstance(first, dict) and isinstance(second, dict):
        deleted, added, not_changed, changed = compare_keys(first, second)
        for key in added:
            new_dict[key] = {
                    STATUS: ADDED,
                    VALUE: second[key]
                    }
        for key in deleted:
            new_dict[key] = {
                    STATUS: DELETED,
                    VALUE: first[key]
                    }
        for key in not_changed:
            new_dict[key] = {
                    STATUS: NOT_CHANGED,
                    VALUE: first[key]
                    }
        for key in changed:
            first_value = first[key]
            second_value = second[key]
            if isinstance(first_value, dict
                    ) and isinstance(second_value, dict):
                inner = {}
                new_dict[key] = {
                        STATUS: HAS_CHILDS,
                        VALUE: inner
                        }
                get_diff(first_value, second_value, inner)
            else:
                new_dict[key] = {
                        STATUS: CHANGED,
                        OLD_VALUE: first_value,
                        VALUE: second_value
                        }
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
