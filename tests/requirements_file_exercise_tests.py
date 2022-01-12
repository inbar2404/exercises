import unittest
from unittest import mock

from src.requirements_file_exercise import read_file_lines


class MyTestCase(unittest.TestCase):
    #TODO: Implement tests
    def test_should_create_libraries_string_from_single_file(self):
        self.assertEqual(True, True)

    def test_should_create_libraries_string_from_file_with_references(self):
        self.assertEqual(True, True)

    def test_should_create_empty_string_for_empty_file(self):
        self.assertEqual(True, True)

    def test_should_read_once_file_that_has_more_than_one_reference(self):
        self.assertEqual(True, True)

    def test_create_libraries_string_raise_file_not_found_error(self):
        self.assertEqual(True, True)

    def test_should_create_libraries_string_from_infinite_recursion_files(self):
        self.assertEqual(True, True)

    # TODO: Consider remove these tests
    def test_read_file_lines_sucsess(self):
        EXPECTED = ['some', 'text is', 'written here']
        text = read_file_lines('test_data/data.txt')
        self.assertEqual(text, EXPECTED)

    # TODO: Consider remove these tests
    @mock.patch('src.requirements_file_exercise.read_file_lines')
    def test_read_file_lines_could_not_find_file(self, mock_read_file_lines):
        mock_read_file_lines.side_effect = FileNotFoundError
        read_file_lines('non_exist_path.txt')

        self.assertTrue(mock_read_file_lines.called)


# TODO: Remove that
if __name__ == '__main__':
    unittest.main()
