import os
import unittest
from settings import ONDOCS_ALIAS
from utils.media.file import *
from mock import patch, MagicMock, mock_open, Mock

class UtilsMediaTest(unittest.TestCase):
    """
    test functions in utils.media.file
    """

    def test_create_file_ok(self):
        result = create_file("/Users/hpineda/Desktop/test_file.txt", 'Hola mundo')
        self.assertTrue(result)

    def test_delete(self):
    	create_file("/Users/hpineda/Desktop/test_file.txt", 'Hola mundo')
    	result = delete('/Users/hpineda/Desktop/test_file.txt')
        self.assertTrue(result)
