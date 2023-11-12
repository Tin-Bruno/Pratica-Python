import unittest
from name_fuction import get_formatted_name


class NmaesTestCase(unittest.TestCase):
    """Testes para' name_function.py'."""

    def test_first_last_name(self):
        """Nomes como 'Janis Joplin' funcionam?"""

        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


unittest.main()
