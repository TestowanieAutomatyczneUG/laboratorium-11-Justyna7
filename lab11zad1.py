# Za pomocą atrap przeprowadź testy aplikacji, która będzie korzystała z operacji na plikach (otwieranie, edytowanie, usuwanie).
#
# Rozwiązanie umieść w serwisie github pod linkiem: https://classroom.github.com/a/j7lrZ3bL



from unittest.mock import mock_open
from unittest import TestCase, main
from unittest.mock import *


class App:
    def open_file(self, filepath):
        return None

    def edit_file(self, filepath):
        return None

    def delete_file(self, filepath):
        return None



class test_App(TestCase):
    def setUp(self):
        self.test_object = App()

    def test_open(self):
        def sideEffect(arg):
            open = mock_open(read_data = "moose")
            with open(arg, 'r') as f:
                return f.read()
        # prepare mock open
        self.test_object.open_file = Mock(name='openFile')
        self.test_object.open_file.side_effect = sideEffect

        # testing
        self.assertEqual("moose", self.test_object.open_file('/fake/file/path.txt'), 'No Files open')

    def test_edit(self):
        # prepare mock open
        self.test_object.edit_file = mock_open()
        with patch('__main__.open', self.test_object.edit_file):
            with open('/fake/file/path.txt', 'w') as f:
                f.write("moose")
        # testing
        self.test_object.edit_file.assert_called_once_with('/fake/file/path.txt', 'w')
        handle = self.test_object.edit_file()
        handle.write.assert_called_once_with('moose')



def tearDown(self):
    self.test_object = None


if __name__ == '__main__':
    main()

