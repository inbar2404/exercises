from typing import List

REFERENCE_TO_REQUIREMENT_FILE_KEY = '-r '


def create_libraries_string(path_to_file: str) -> str:
    libraries: List[str] = []
    files_to_scan: List[str] = [path_to_file]
    scanned_files: List[str] = []

    for current_file in files_to_scan:
        if current_file not in scanned_files:
            text: List[str] = read_file_lines(current_file)
            libraries = get_libraries_list(text, libraries, files_to_scan)
            scanned_files.append(current_file)

    return ' '.join(libraries)


def get_libraries_list(lines: List[str], libraries: List[str], files_to_scan: List[str]) -> List[str]:
    for current_line in lines:
        current_line: str = current_line.strip()
        if current_line.startswith(REFERENCE_TO_REQUIREMENT_FILE_KEY):
            files_to_scan.append(get_file_name_from_line(current_line))
        elif get_package_name_from_line(current_line) not in libraries:
            libraries.append(get_package_name_from_line(current_line))
    return libraries


def read_file_lines(path_to_file: str) -> List[str]:
    with open(path_to_file) as file:
        lines = [line for line in file.read().splitlines() if line]
    return lines


def get_package_name_from_line(line: str) -> str:
    return line.replace(" ", "").split('==')[0]


def get_file_name_from_line(line: str) -> str:
    return line.replace(REFERENCE_TO_REQUIREMENT_FILE_KEY, "").replace(" ", "")
