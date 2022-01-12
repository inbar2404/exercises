import yaml
import ez_yaml


def get_dict_from_data(data) -> dict:
    dict_to_compare = data
    # TODO: Find pretty way to do that
    if isinstance(data, list):
        dict_to_compare = data[0]
    return dict_to_compare


def merge_to_main_dict(main_dict: dict, data):
    dict_to_compare: dict = get_dict_from_data(data)
    if main_dict.keys() == dict_to_compare.keys():
        if isinstance(data, list):
            return [main_dict]+data
        return [main_dict, data]
    return None


def merge_to_dict(main_dict: dict, data_to_add) -> list:
    data_after_merge = merge_to_main_dict(main_dict, data_to_add)
    if data_after_merge is not None:
        return data_after_merge

    for key, value in main_dict.items():
        if isinstance(value, list) and len(value) > 0:
            value = value[0]
        if isinstance(value, dict):
            data_after_merge = merge_to_dict(value, data_to_add)
            if data_after_merge is not None:
                main_dict[key] = data_after_merge
                return main_dict
    return None


def merge_yamls(main_yaml_file_path: str, configuration_to_add: str):
    # TODO: Handle case files not found?
    with open(main_yaml_file_path) as file:
        main_yaml = yaml.full_load(file)
    yaml_to_add = yaml.safe_load(configuration_to_add)

    result = merge_to_dict(main_yaml, yaml_to_add)
    if result is None:
        # TODO: Handle here case that 'yaml_to_add' is list!!!
        main_yaml.update(yaml_to_add)
        result = main_yaml

    ez_yaml.to_file(result, file_path=main_yaml_file_path)
