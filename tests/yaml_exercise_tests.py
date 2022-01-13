import unittest
from unittest import mock

import yaml

from src.yaml_exercise import merge_yamls


class YamlExerciseTest(unittest.TestCase):
    def test_should_add_dict_with_existing_keys_and_new_values_as_list_to_main_yaml(self):
        self.assertEqual(True, False)  # TODO

    def test_should_add_dict_with_some_of_existing_keys_but_not_all_in_the_end_main_yaml(self):
        self.assertEqual(True, False)  # TODO

    def test_should_add_dict_with_existing_keys_and_few_new_keys_in_the_end_main_yaml(self):
        self.assertEqual(True, False)  # TODO

    def test_should_add_dict_with_new_keys_in_the_end_of_the_main_yaml(self):
        self.assertEqual(True, False)  # TODO

    def test_should_add_list_with_one_item_to_existing_list_in_main_yaml(self):
        self.assertEqual(True, False)  # TODO

    def test_should_add_list_with_more_than_one_item_to_existing_list_in_main_yaml(self):
        self.assertEqual(True, False)  # TODO

    def test_should_add_list_that_contains_new_dict_in_the_end_of_the_main_yaml(self):
        self.assertEqual(True, False)  # TODO

    @mock.patch('src.yaml_exercise.read_data_from_main_yaml')
    def test_main_yaml_should_not_change_when_try_to_add_empty_config(self, mock_data_from_main_yaml):
        configuration_to_add = """ """
        expected = {
                    'name' : 'inbar',
                    'job' : ['programmer', 'student'],
                    'address' : {'country': 'Israel',
                                 'city': 'Hod-Hashron'}
                   }
        mock_data_from_main_yaml.return_value = expected

        merge_yamls('main_yaml.yaml', configuration_to_add)
        actual = yaml.safe_load(open('main_yaml.yaml').read())

        self.assertEqual(actual, expected)

    def test_main_yaml_should_not_change_when_try_to_add_the_exact_nested_dict(self):
        self.assertEqual(True, False) #TODO

    def test_merge_yamls_raise_exception_when_not_found_file(self):
        self.assertEqual(True, False)  # TODO