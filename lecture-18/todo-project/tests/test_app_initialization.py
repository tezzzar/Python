import unittest
from unittest.mock import patch, mock_open, MagicMixin
from todo.config import _init_config_file, _create_database, init_app

from todo import DB_READ_ERROR, DB_WRITE_ERROR, FILE_ERROR, SUCCESS, DIR_ERROR

from pathlib import Path

test_db_path = Path.home().joinpath('.' + Path.home().stem + "_todo.json")

class TestAppInitialization(unittest.TestCase):
    
    @patch('pathlib.Path.mkdir')
    @patch('pathlib.Path.touch')
    def test_init_config_file_success(self, mock_touch, mock_mkdir):
        mock_mkdir.return_value = None
        mock_touch.return_value = None
        result = _init_config_file()
        self.assertEqual(result, SUCCESS)
        mock_mkdir.assert_called_once_with(exist_ok=True)
        mock_touch.assert_called_once_with(exist_ok=True)


    @patch('pathlib.Path.mkdir')
    @patch('pathlib.Path.touch')
    def test_init_config_file_dir_error(self, mock_touch, mock_mkdir):
        mock_mkdir.side_effect = OSError
        result = _init_config_file()
        self.assertEqual(result, DIR_ERROR)
        mock_mkdir.assert_called_once_with(exist_ok=True)
        mock_touch.assert_not_called()

    @patch('pathlib.Path.mkdir')
    @patch('pathlib.Path.touch')
    def test_init_config_file_file_error(self, mock_touch, mock_mkdir):
        mock_mkdir.return_value = None
        mock_touch.side_effect = OSError
        result = _init_config_file()
        self.assertEqual(result, FILE_ERROR)
        mock_mkdir.assert_called_once_with(exist_ok=True)
        mock_touch.assert_called_once_with(exist_ok=True)

