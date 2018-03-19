import unittest

from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('Jacky', 'Wu')
        self.assertEqual(formatted_name, 'Jacky Wu')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('Jacky', 'Wu', 'X')
        self.assertEqual(formatted_name, 'Jacky X Wu')

unittest.main()