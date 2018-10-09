import unittest
import Main
#from unittest import TestCase


class TestAddNumbers(unittest.TestCase):
    def test_addNumbers(self):
        addResult = Main.addNumbers(10, 20)
        self.assertEqual(30, addResult)

    def test_Remainder(self):
        remainderResult = Main.getRemainder(11, 5)
        self.assertEqual(1, remainderResult)

if __name__ == '__main__':
    unittest.main()