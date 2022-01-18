from typing import List

from src.requirementsFileExercise.package import Package
from src.requirementsFileExercise.file_reader import read_file_lines


def create_libraries_string(file_name: str) -> str:
    libraries: List[str] = []
    requirements_files: List[str] = [file_name]
    scanned_files: List[str] = []

    for requirements_file in requirements_files:
        if requirements_file not in scanned_files:
            text: List[str] = read_file_lines(requirements_file)
            file_libraries, files_references = _create_libraries_list(text)
            libraries += file_libraries
            requirements_files += files_references
            scanned_files.append(requirements_file)

    return ' '.join([str(library) for library in libraries])


def _add_package(libraries: List[Package], package: Package):
    for library in libraries:
        if library.name == package.name:
            if library.version != package.version:
                library.version = max(library.version, package.version)
                return
    libraries.append(package)


def _create_libraries_list(lines: List[str]) -> List[str]:
    files: List[str] = []
    libraries: List[str] = []
    for line in lines:
        file_name: str = Package.get_file_name(line)
        if file_name:
            files.append(file_name)
        else:
            package: Package = Package.get_package(line)
            _add_package(libraries, package)
    return libraries, files
