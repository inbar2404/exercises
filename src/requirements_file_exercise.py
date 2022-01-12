from typing import List
from pip._internal.req import parse_requirements, InstallRequirement
import os.path
# TODO: Don't forget to update requirements.txt

REQUIREMENTS_FILE_KEY = 'requirements'


def create_libraries_string(path_to_file: str) -> str:
    scanned_files: List[str] = [path_to_file]
    libraries_list: List[str] = get_libraries_list(path_to_file, scanned_files)
    # TODO: Find a pretty way to do that
    return ' '.join(libraries_list)


# TODO: Maybe update typing in case of error handling
def get_libraries_list(path_to_file: str, scanned_files: List[str]) -> List[str]:
    try:
        libraries: List[str] = []
        requirements: List[InstallRequirement] = parse_requirements(path_to_file, session=False)

        for current_requirement in requirements:
            # TODO: IMPORTANT! Right now I assume that requirements file will seems like that: '...requirements... .txt' I should read about it and understand what is the best solution
            # TODO: Think about a pretty why to check this condition
            if REQUIREMENTS_FILE_KEY in current_requirement.req.name and \
               os.path.exists(current_requirement.req.name) and \
               current_requirement.req.name not in scanned_files:
                scanned_files.append(current_requirement.req.name)
                libraries.extend(get_libraries_list(current_requirement.req.name, scanned_files))
            elif current_requirement.req.name not in libraries:
                libraries.append(current_requirement.req.name)

        return libraries
    # TODO: Maybe better error-handling, i.e: case of file not exist is most common
    except Exception:
        raise