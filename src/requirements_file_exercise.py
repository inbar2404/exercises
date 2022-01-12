from typing import List
from pip._internal.req import parse_requirements, InstallRequirement
import os.path
# TODO: Don't forget to update requirements.txt


def create_libraries_string(path_to_file: str) -> str:
    # TODO: Find a pretty way to do that
    return ' '.join(get_libraries_list(path_to_file))


# TODO: Maybe update typing in case of error handling
def get_libraries_list(path_to_file: str) -> List[str]:
    try:
        libraries: List[str] = []
        requirements: List[InstallRequirement] = parse_requirements(path_to_file, session=False)

        for current_requirement in requirements:
            if 'requirements' in current_requirement.req.name and os.path.exists(current_requirement.req.name):
                libraries.extend(get_libraries_list(current_requirement.req.name))
            else:
                libraries.append(current_requirement.req.name)

        return libraries
    # TODO: Maybe better error-handling, i.e: case of file not exist is most common
    except Exception:
        raise
