import unittest
from name_function import get_formatted_name

class CaseTestNameFunction(unittest.TestCase):
    def test_get_formatted_name(self):
        formatname = get_formatted_name("tom", "nick")
        self.assertEqual(formatname, "Tom Nick")

unittest.main