#!/usr/bin/python3
import unittest

from GetElement import GetElement

class Tests(unittest.TestCase):
    def testcase_pass_1(self):
        array = [1,2,3,4,5]
        index = 0

        result = GetElement(array, index)
        self.assertEqual(result, 1)
        print("testcase_pass_1 passed!")
    
    def testcase_pass_2(self):
        array = ['a', 'b', 'c', 'd', 'e']
        index = 3

        result = GetElement(array, index)
        self.assertEqual(result, 'd')
        print("testcase_pass_2 passed!")
    
    def testcase_pass_3(self):
        array = ['a', 'b', 1, 2, 'c']
        index = 2

        result = GetElement(array, index)
        self.assertEqual(result, 1)
        print("testcase_pass_3 passed!")

if __name__ == '__main__':
    unittest.main()
    