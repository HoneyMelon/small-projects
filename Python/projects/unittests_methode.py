from methode import *
import unittest


class MethodeUnittest(unittest.TestCase):
    def test_c1(self):
        self.assertEqual(methode(0, 0, 0), 3, 'Error in c1 test (0, 0, 0)')
        self.assertEqual(methode(3, 3, 0), 0, 'Error in c1 test (3, 3, 0)')
        self.assertEqual(methode(0, 1, 0), 3, 'Error in c1 test (0, 1, 0)')

    def test_c3b(self):
        self.assertEqual(methode(3, 3, 0), 0, 'Error in c3b test (3, 3, 0)')
        self.assertEqual(methode(3, 3, 4), -2, 'Error in c3b test (3, 3, 4)')
        self.assertEqual(methode(3, 0, 0), 0, 'Error in c3b test (3, 0, 0)')
        self.assertEqual(methode(3, 0, 4), -4, 'Error in c3b test (3, 0, 4)')
        self.assertEqual(methode(0, 3, 0), 0, 'Error in c3b test (0, 3, 0)')
        self.assertEqual(methode(0, 3, 4), -4, 'Error in c3b test (0, 3, 4)')
        self.assertEqual(methode(0, 0, 0), 3, 'Error in c3b test (0, 0, 0)')
        self.assertEqual(methode(0, 0, 4), 3, 'Error in c3b test (0, 0, 4)')


if __name__ == '__main__':
    unittest.main()
