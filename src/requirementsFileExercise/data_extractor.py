REFERENCE_TO_REQUIREMENT_FILE_KEY = '-r '


def get_package(str: str) -> str:
    return str.replace(" ", "").split('==')[0]


def get_file_name(str: str) -> str:
    return str.replace(REFERENCE_TO_REQUIREMENT_FILE_KEY, "").replace(" ", "")


def has_requirement_file_reference(str: str) -> bool:
    return str.startswith(REFERENCE_TO_REQUIREMENT_FILE_KEY)
