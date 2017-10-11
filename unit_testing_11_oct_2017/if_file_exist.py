import os.path
import unittest

class TestFile(unittest.TestCase):
    """
        test class to check if file is present in the file path or not
    """

    def if_file_exist(self):
        file_path = '/tmp/dgplug.txt'
        self.assertTrue(os.path.exists(file_path)

if __name__ == '__main__':
        unittest.main()
