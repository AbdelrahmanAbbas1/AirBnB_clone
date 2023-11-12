#!/usr/bin/python3
"""A unnitest for console"""
import unittest
from unittest.mock import patch
from io import StringIO
from your_command_interpreter_module import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.cmd = HBNBCommand()
        self.base_model = "BaseModel"
        self.obj_id = "test_id"
        self.obj_str = f'{{"__class__": "{self.base_model}", "id": "{self.obj_id}"}}\n'

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, mock_stdout):
        self.cmd.onecmd(expected_output)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_do_create(self):
        with patch('models.base_model.BaseModel.save') as mock_save:
            self.assert_stdout(f"create {self.base_model}", "Instance created: test_id\n")
            mock_save.assert_called_once()

    @patch('models.storage.all')
    def test_do_show_found(self, mock_all):
        mock_all.return_value = {self.obj_id: json.loads(self.obj_str)}
        self.assert_stdout(f"show {self.base_model} {self.obj_id}\n", self.obj_str)

    @patch('models.storage.all')
    def test_do_show_not_found(self, mock_all):
        mock_all.return_value = {}
        self.assert_stdout(f"show {self.base_model} {self.obj_id}\n", "Object not found\n")

    def test_do_quit(self):
        self.assertTrue(self.cmd.onecmd("quit"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        self.assertTrue(self.cmd.onecmd("EOF"))
        self.assertEqual(mock_stdout.getvalue(), "\n")


if __name__ == '__main__':
    unittest.main()
