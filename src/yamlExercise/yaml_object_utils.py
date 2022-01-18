def chain(first_yaml_object, second_yaml_object):
    if isinstance(second_yaml_object, list):
        while len(second_yaml_object) > 0:
            first_yaml_object.update(second_yaml_object.pop())
    else:
        first_yaml_object.update(second_yaml_object)
    return first_yaml_object


def merge(first_yaml_object: dict, second_yaml_object):
    if isinstance(second_yaml_object, list):
        dict_data: dict = _convert_to_dict(second_yaml_object)
        if first_yaml_object.keys() == dict_data.keys():
            return [first_yaml_object] + second_yaml_object
    return None


def deep_merge(yaml_dict: dict, data) -> list:
    merged_date = merge(yaml_dict, data)
    if merged_date is not None:
        return merged_date

    for key, value in yaml_dict.items():
        if isinstance(value, list) and len(value) > 0:
            value = value[0]
        if isinstance(value, dict):
            merged_date = deep_merge(value, data)
            if merged_date is not None:
                yaml_dict[key] = merged_date
                return yaml_dict
    return None


def _convert_to_dict(yaml_object) -> dict:
    if yaml_object is None:
        return {}
    if isinstance(yaml_object, list):
        return yaml_object[0]
    return yaml_object
