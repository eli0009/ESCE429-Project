import unittest

import request


def getListLength(l):
    return len(l)

class TestYourFunctions(unittest.TestCase):

    def testEmptyList(self):
        input_list = []
        self.assertEqual(getListLength(input_list), 0)
    
    def testList(self):
        input_list = [1,2,3]
        self.assertEqual(getListLength(input_list), 3)
    
    def testListFalse(self):
        input_list = [1,2,3]
        self.assertNotEqual(getListLength(input_list), 3)

    def testListTrue(self):
        input_list = [1,2,3]
        self.assertEqual(getListLength(input_list), 4)

if __name__ == "__main__":
    unittest.main()