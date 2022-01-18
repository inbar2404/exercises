REFERENCE_TO_REQUIREMENT_FILE_KEY = '-r '
VERSIONS_COMPARE_SYMBOLS = ['==', '>=', '~=']


def get_package(str: str) -> str:
    version_format: str = get_package_version(str)
    if version_format != '':
        return str.replace(" ", "").split(_get_compare_symbol(str))[0] + '-' + version_format
    return str.replace(" ", "")


def get_package_version(str: str) -> str:
    compare_symbol: str = _get_compare_symbol(str)
    if compare_symbol != '':
        return str.split(_get_compare_symbol(str))[1].replace(" ", "")
    return ''


def _get_compare_symbol(str: str) -> str:
    for symbol in VERSIONS_COMPARE_SYMBOLS:
        if symbol in str:
            return symbol
    return ''


def get_file_name(str: str) -> str:
    return str.replace(REFERENCE_TO_REQUIREMENT_FILE_KEY, "").replace(" ", "")


def has_requirement_file_reference(str: str) -> bool:
    return str.startswith(REFERENCE_TO_REQUIREMENT_FILE_KEY)
