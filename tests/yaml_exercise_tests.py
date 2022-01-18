import unittest
from unittest import mock
import yaml
from src.yamlExercise.yaml_exercise import merge_yaml


class YamlExerciseTest(unittest.TestCase):
    @mock.patch('src.yamlExercise.yaml_exercise.read_from_file')
    def test_should_add_dict_with_existing_keys_in_the_end_of_yaml(self, mock_data_from_yaml):
        configuration_to_add = """
         country: 'USA'
         city: 'New-York'
         """
        file_name = 'main_yaml.yaml'
        mock_data_from_yaml.return_value = {
            'name': 'inbar',
            'address': {'country': 'Israel',
                        'city': 'Hod-Hashron'},
            'job': ['programmer', 'student']
        }
        expected = {
            'name': 'inbar',
            'address': {'country': 'Israel',
                        'city': 'Hod-Hashron'},
            'job': ['programmer', 'student'],
            'country': 'USA',
            'city': 'New-York'
        }

        merge_yaml(file_name, configuration_to_add)
        actual = yaml.safe_load(open(file_name).read())

        self.assertEqual(expected, actual)

    @mock.patch('src.yamlExercise.yaml_exercise.read_from_file')
    def test_should_add_list_with_multiple_items_to_existing_list_in_yaml(self, mock_data_from_yaml):
        configuration_to_add = """
         - occupation: 'student'
           place: 'OPU'
         - occupation: 'private-teacher'
           place: 'home'
         """
        file_name = 'main_yaml.yaml'
        expected = {
                    'name' : 'inbar',
                    'job' : [{'occupation':'programmer', 'place':'IDF'},
                             {'occupation':'student', 'place': 'OPU'},
                             {'occupation': 'private-teacher', 'place': 'home'}],
                    'address' : {'country': 'Israel',
                                 'city': 'Hod-Hashron'}
                   }
        mock_data_from_yaml.return_value = {
                    'name' : 'inbar',
                    'job' : [{'occupation':'programmer', 'place':'IDF'}],
                    'address' : {'country': 'Israel',
                                 'city': 'Hod-Hashron'}
                   }

        merge_yaml(file_name, configuration_to_add)
        actual = yaml.safe_load(open(file_name).read())

        self.assertEqual(actual, expected)

    @mock.patch('src.yamlExercise.yaml_exercise.read_from_file')
    def test_add_list_contains_new_dict_in_the_end_of_yaml(self, mock_data_from_yaml):
        configuration_to_add = """
         - relationship: 'mother'
           full-name: 'Efrat'
         """
        file_name = 'main_yaml.yaml'
        mock_data_from_yaml.return_value = {
                                                'name' : 'inbar',
                                                'job' : [{'occupation':'programmer', 'place':'IDF'}],
                                                'address' : {'country': 'Israel',
                                                             'city': 'Hod-Hashron'}
                                                }
        expected = {
                    'name' : 'inbar',
                    'job' : [{'occupation':'programmer', 'place':'IDF'}],
                    'address' : {'country': 'Israel',
                                 'city': 'Hod-Hashron'},
                    'relationship': 'mother',
                    'full-name': 'Efrat'
                   }

        merge_yaml(file_name, configuration_to_add)
        actual = yaml.safe_load(open(file_name).read())

        self.assertEqual(actual, expected)

    @mock.patch('src.yamlExercise.yaml_exercise.read_from_file')
    def test_yaml_not_change_when_add_empty_configuration(self, mock_data_from_yaml):
        configuration_to_add = """ """
        file_name = 'main_yaml.yaml'
        expected = {
                    'name' : 'inbar',
                    'job' : ['programmer', 'student'],
                    'address' : {'country': 'Israel',
                                 'city': 'Hod-Hashron'}
                   }
        mock_data_from_yaml.return_value = expected.copy()

        merge_yaml(file_name, configuration_to_add)
        actual = yaml.safe_load(open(file_name).read())

        self.assertEqual(actual, expected)

    @mock.patch('src.yamlExercise.yaml_exercise.read_from_file')
    def test_merge_yaml_raise_exception_when_not_found_file(self, mock_yaml_data):
        mock_yaml_data.side_effect = FileNotFoundError
        self.assertRaises(FileNotFoundError, merge_yaml, 'no_exist.yaml', """dfdfdf""")
