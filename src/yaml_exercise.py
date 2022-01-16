import yaml
import ez_yaml


def merge_yaml(yaml_file: str, additional_configuration: str):
    yaml = read_data_from_yaml(yaml_file)
    additional_yaml = yaml.safe_load(additional_configuration)

    result = yaml
    if additional_yaml is not None:
        if yaml is None or yaml == {}:
            result = additional_yaml
        else:
            result = deep_merge_yaml(yaml, additional_yaml)
            if result is None:
                result = chain_additional_config_to_yaml(yaml, additional_yaml)

    ez_yaml.to_file(result, file_path=yaml_file)


def chain_additional_config_to_yaml(yaml, additional_yaml):
    if isinstance(additional_yaml, list):
        while len(additional_yaml) > 0:
            yaml.update(additional_yaml.pop())
    else:
        yaml.update(additional_yaml)
    return yaml


def read_data_from_yaml(file_name: str):
    with open(file_name) as file:
        return yaml.full_load(file)


def data_to_dict(data) -> dict:
    if data is None:
        return {}
    if isinstance(data, list):
        return data[0]
    return data


def merge_dict(dict: dict, data):
    dict_data: dict = data_to_dict(data)
    if dict.keys() == dict_data.keys():
        if isinstance(data, list):
            return [dict]+data
        return [dict, data]
    return None


def deep_merge_yaml(yaml_dict: dict, data) -> list:
    merged_date = merge_dict(yaml_dict, data)
    if merged_date is not None:
        return merged_date

    for key, value in yaml_dict.items():
        if isinstance(value, list) and len(value) > 0:
            value = value[0]
        if isinstance(value, dict):
            merged_date = deep_merge_yaml(value, data)
            if merged_date is not None:
                yaml_dict[key] = merged_date
                return yaml_dict
    return None
