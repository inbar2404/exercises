from typing import List
# TODO: Don't forget to update requirements.txt

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


def read_file_lines(path_to_file: str) -> List[str]:
    with open(path_to_file) as file:
        lines = [line for line in file.read().splitlines() if line]
        file.close()
    return lines


def get_libraries_list(lines: List[str], libraries: List[str], files_to_scan: List[str]) -> List[str]:
    for current_line in lines:
        current_line = current_line.strip()
        if current_line.startswith(REFERENCE_TO_REQUIREMENT_FILE_KEY):
            files_to_scan.append(current_line.replace(REFERENCE_TO_REQUIREMENT_FILE_KEY, "").replace(" ", ""))  # TODO: Think about a pretty way
        elif current_line.strip() not in libraries:
            libraries.append(current_line.replace(" ", "").split('==')[0])  # TODO: Think about a pretty way
    return libraries
