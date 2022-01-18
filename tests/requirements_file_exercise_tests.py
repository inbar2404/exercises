import unittest
from unittest import mock
from unittest.mock import call

from src.requirementsFileExercise.requirements_file_exercise import create_libraries_string


class RequirementsFileExerciseTest(unittest.TestCase):
    @mock.patch('src.requirementsFileExercise.requirements_file_exercise.read_file_lines')
    def test_create_libraries_string_from_single_file(self, mock_read_file_lines):
        mock_read_file_lines.return_value = ["Flask ==2.0.2", "  Flask-RESTful", "Jinja2==  3.0.2",
                                             "validators>=0.18.2", "typing-extensions~=3.10.0.2 "]
        file_name = 'path_to_rquirements_file.txt'
        excepted = "Flask-2.0.2 Flask-RESTful Jinja2-3.0.2 validators-0.18.2 typing-extensions-3.10.0.2"

        actual = create_libraries_string(file_name)

        mock_read_file_lines.assert_called_once_with(file_name)
        self.assertEqual(excepted, actual)

    @mock.patch('src.requirementsFileExercise.requirements_file_exercise.read_file_lines')
    def test_create_libraries_string_from_multiple_files(self, mock_read_file_lines):
        referenced_requirement_file = 'test-requirements.txt'
        mock_lines_of_first_requirement_file = ["Flask==2.0.2", "Flask-RESTful==0.3.9", "Jinja2==3.0.2",
                                                "-r " + referenced_requirement_file, "validators==0.18.2"]
        mock_lines_of_second_requirement_file = ["requests==2.26.0", "six==1.16.0", "typing-extensions==3.10.0.2"]
        mock_read_file_lines.side_effect = [mock_lines_of_first_requirement_file, mock_lines_of_second_requirement_file]
        main_requirements_file = 'requirements_file.txt'
        excepted = "Flask-2.0.2 Flask-RESTful-0.3.9 Jinja2-3.0.2 validators-0.18.2 requests-2.26.0 six-1.16.0 " \
                   "typing-extensions-3.10.0.2"

        actual = create_libraries_string(main_requirements_file)

        mock_read_file_lines.assert_has_calls([call(main_requirements_file), call(referenced_requirement_file)])
        self.assertEqual(excepted, actual)

    @mock.patch('src.requirementsFileExercise.requirements_file_exercise.read_file_lines')
    def test_create_libraries_string_add_just_one_instance_of_library_to_list(self, mock_read_file_lines):
        mock_read_file_lines.return_value = ["Flask==2.0.2", "Flask-RESTful==0.3.9", "Jinja2==3.0.2",
                                             "validators==0.18.2", "Flask==2.0.2", "Jinja2==3.0.2"]
        file_name = 'path_to_rquirements_file.txt'
        excepted = "Flask-2.0.2 Flask-RESTful-0.3.9 Jinja2-3.0.2 validators-0.18.2"

        actual = create_libraries_string(file_name)

        mock_read_file_lines.assert_called_once_with(file_name)
        self.assertEqual(excepted, actual)

    @mock.patch('src.requirementsFileExercise.requirements_file_exercise.read_file_lines')
    def test_should_create_empty_string_for_empty_file(self, mock_read_file_lines):
        excepted = ""
        mock_read_file_lines.return_value = []
        file_name = 'path_to_rquirements_file.txt'

        actual = create_libraries_string(file_name)

        mock_read_file_lines.assert_called_once_with(file_name)
        self.assertEqual(excepted, actual)

    @mock.patch('src.requirementsFileExercise.requirements_file_exercise.read_file_lines')
    def test_create_libraries_string_from_multiple_files(self, mock_read_file_lines):
        first_requirements_file = 'requirements.txt'
        second_requirements_file = 'second-requirements.txt'
        third_requirements_file = 'third-requirements.txt'
        mock_lines_of_first_requirement_file = ["Flask==2.0.2", "-r " + second_requirements_file, "Jinja2==3.0.2",
                                                "-r " + third_requirements_file, "validators==0.18.2"]
        mock_lines_of_second_requirement_file = ["requests==2.26.0", "-r " + third_requirements_file,
                                                 "typing-extensions==3.10.0.2"]
        mock_lines_of_third_requirement_file = ["six==1.16.0", "Flask-RESTful==0.3.9", "redis==2.10.6", "-r " + first_requirements_file]
        mock_read_file_lines.side_effect = [mock_lines_of_first_requirement_file, mock_lines_of_second_requirement_file,
                                            mock_lines_of_third_requirement_file]
        excepted = "Flask-2.0.2 Jinja2-3.0.2 validators-0.18.2 requests-2.26.0 typing-extensions-3.10.0.2 six-1.16.0 " \
                   "Flask-RESTful-0.3.9 redis-2.10.6"

        actual = create_libraries_string(first_requirements_file)

        mock_read_file_lines.assert_has_calls([call(first_requirements_file), call(second_requirements_file),
                                               call(third_requirements_file)])
        self.assertEqual(mock_read_file_lines.call_count, 3)
        self.assertEqual(excepted, actual)

    @mock.patch('src.requirementsFileExercise.requirements_file_exercise.read_file_lines')
    def test_should_create_libraries_string_that_referenced_file_has_reference_to_more_file(self, mock_read_file_lines):
        first_requirements_file = 'requirements.txt'
        second_requirements_file = 'second-requirements.txt'
        third_requirements_file = 'third-requirements.txt'
        mock_lines_of_first_requirement_file = ["Flask==2.0.2", "Jinja2==3.0.2", "-r " + second_requirements_file,
                                                "validators==0.18.2"]
        mock_lines_of_second_requirement_file = ["requests==2.26.0", "-r " + third_requirements_file,
                                                 "typing-extensions==3.10.0.2"]
        mock_lines_of_third_requirement_file = ["six==1.16.0", "Flask-RESTful==0.3.9", "redis==2.10.6"]
        mock_read_file_lines.side_effect = [mock_lines_of_first_requirement_file, mock_lines_of_second_requirement_file,
                                            mock_lines_of_third_requirement_file]
        excepted = "Flask-2.0.2 Jinja2-3.0.2 validators-0.18.2 requests-2.26.0 typing-extensions-3.10.0.2 six-1.16.0 " \
                   "Flask-RESTful-0.3.9 redis-2.10.6"

        actual = create_libraries_string(first_requirements_file)

        mock_read_file_lines.assert_has_calls([call(first_requirements_file), call(second_requirements_file),
                                               call(third_requirements_file)])
        self.assertEqual(mock_read_file_lines.call_count, 3)
        self.assertEqual(excepted, actual)

    @mock.patch('src.requirementsFileExercise.requirements_file_exercise.read_file_lines')
    def test_create_libraries_string_should_raise_file_not_found_error(self, mock_read_file_lines):
        mock_read_file_lines.side_effect = FileNotFoundError
        self.assertRaises(FileNotFoundError, create_libraries_string, "no_exist.txt")
