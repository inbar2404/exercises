from typing import List

from src.requirementsFileExercise.data_extractor import get_file_name, get_package, has_requirement_file_reference
from src.requirementsFileExercise.file_reader import read_file_lines


def create_libraries_string(file_name: str) -> str:
    libraries: List[str] = []
    files: List[str] = [file_name]
    scanned_files: List[str] = []

    for file in files:
        if file not in scanned_files:
            text: List[str] = read_file_lines(file)
            file_libraries, files_references = _create_libraries_list(text)
            libraries += file_libraries
            files += files_references
            scanned_files.append(file)

    return ' '.join(libraries)


def _create_libraries_list(lines: List[str]) -> List[str]:
    files: List[str] = []
    libraries: List[str] = []
    for line in lines:
        line: str = line.strip()
        if has_requirement_file_reference(line):
            files.append(get_file_name(line))
        elif get_package(line) not in libraries:
            libraries.append(get_package(line))
    return libraries, files
