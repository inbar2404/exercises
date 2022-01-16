from typing import List

REFERENCE_TO_REQUIREMENT_FILE_KEY = '-r '


def create_libraries_string(file_name: str) -> str:
    libraries: List[str] = []
    files: List[str] = [file_name]
    scanned_files: List[str] = []

    for file in files:
        if file not in scanned_files:
            text: List[str] = read_file_lines(file)
            libraries = create_libraries_list(text, libraries, files)
            scanned_files.append(file)

    return ' '.join(libraries)


def create_libraries_list(lines: List[str], libraries: List[str], files: List[str]) -> List[str]:
    for line in lines:
        line: str = line.strip()
        if line.startswith(REFERENCE_TO_REQUIREMENT_FILE_KEY):
            files.append(get_file_name_from_line(line))
        elif get_package_name_from_line(line) not in libraries:
            libraries.append(get_package_name_from_line(line))
    return libraries


def read_file_lines(file_name: str) -> List[str]:
    with open(file_name) as file:
        lines = [line for line in file.read().splitlines() if line]
    return lines


def get_package_name_from_line(line: str) -> str:
    return line.replace(" ", "").split('==')[0]


def get_file_name_from_line(line: str) -> str:
    return line.replace(REFERENCE_TO_REQUIREMENT_FILE_KEY, "").replace(" ", "")
