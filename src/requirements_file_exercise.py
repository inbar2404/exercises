import yaml
import ez_yaml
# TODO: Create requirements.txt


def find_dict(main_dict: dict, to_add):
    dict_to_compare = to_add
    # TODO: Find pretty way to do that
    if isinstance(to_add, list):
        dict_to_compare = to_add[0]
    if main_dict.keys() == dict_to_compare.keys():
        if isinstance(to_add, list):
            # TODO: Find pretty way to do that
            full_list = [main_dict]
            full_list.extend(to_add)
            return full_list
        return [main_dict, to_add]

    for key, value in main_dict.items():
        if isinstance(value, list) and len(value) > 0:
            value = value[0]
        if isinstance(value, dict):
            result = find_dict(value, to_add)
            if result is not None:
                main_dict[key] = result
                return main_dict

    return None


# TODO: Should I get both yamls as files?
# TODO: Fix conventions
def merge_yamls(main_yaml_file: str, yaml_configuration_to_add_file: str):
    # TODO: Handle case files not found?
    with open(main_yaml_file) as fp:
        main_yaml = yaml.full_load(fp)
    with open(yaml_configuration_to_add_file) as fp:
        yaml_to_add = yaml.full_load(fp)

    result = find_dict(main_yaml, yaml_to_add)
    if result is None:
        # TODO: Handle here case that 'yaml_to_add' is list!!!
        main_yaml.update(yaml_to_add)
        result = main_yaml

    # TODO: It will be better update the original main yaml file
    ez_yaml.to_file(result, file_path='finaly.yaml')
