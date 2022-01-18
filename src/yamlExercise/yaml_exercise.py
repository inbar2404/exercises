import ez_yaml

from src.yamlExercise.yaml_reader import read_from_file, read_from_string
from src.yamlExercise.yaml_object_utils import chain, deep_merge


def merge_yaml(yaml_file: str, additional_configuration: str):
    yaml_data = read_from_file(yaml_file)
    additional_yaml = read_from_string(additional_configuration)

    result = yaml_data
    if additional_yaml is not None:
        if yaml_data is None or yaml_data == {}:
            result = additional_yaml
        else:
            result = deep_merge(yaml_data, additional_yaml)
            if result is None:
                result = chain(yaml_data, additional_yaml)

    ez_yaml.to_file(result, file_path=yaml_file)
