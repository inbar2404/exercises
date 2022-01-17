import yaml


def read_from_file(file_name: str):
    with open(file_name) as file:
        return yaml.full_load(file)


def read_from_string(yaml_content: str):
    return yaml.safe_load(yaml_content)