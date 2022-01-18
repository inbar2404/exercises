class Package(object):
    REFERENCE_TO_REQUIREMENT_FILE_KEY = '-r '
    VERSIONS_COMPARE_SYMBOLS = ['==', '>=', '~=']

    def __init__(self, name: str, version: str = None):
        self._name = name
        self._version = version

    @property
    def name(self):
        return self._name

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, new_version: str):
        self._version = new_version

    def __repr__(self):
        if self._version:
            return self._name + '-' + self._version
        return self._name

    @staticmethod
    def get_package(str: str):
        return Package(Package.__get_package_name(str), Package.__get_package_version(str))

    @staticmethod
    def get_file_name(str: str) -> str:
        if Package.__has_requirement_file_reference(str.strip()):
            return str.strip().replace(Package.REFERENCE_TO_REQUIREMENT_FILE_KEY, "").replace(" ", "")

    def __get_package_name(str: str) -> str:
        compare_symbol: str = Package.__get_compare_symbol(str)
        if compare_symbol != '':
            return str.replace(" ", "").split(compare_symbol)[0]
        return str.replace(" ", "")

    def __get_package_version(str: str) -> str:
        compare_symbol: str = Package.__get_compare_symbol(str)
        if compare_symbol != '':
            return str.split(Package.__get_compare_symbol(str))[1].replace(" ", "")
        return ''

    def __get_compare_symbol(str: str) -> str:
        for symbol in Package.VERSIONS_COMPARE_SYMBOLS:
            if symbol in str:
                return symbol
        return ''

    def __has_requirement_file_reference(str: str) -> bool:
        return str.startswith(Package.REFERENCE_TO_REQUIREMENT_FILE_KEY)