from typing import List


def read_file_lines(file_name: str) -> List[str]:
    with open(file_name) as file:
        lines: List[str] = [line for line in file.read().splitlines() if line]
    return lines
