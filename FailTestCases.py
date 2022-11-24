#!/usr/bin/python3
import unittest

from GetElement import GetElement

class Tests(unittest.TestCase):
    def testcase_fail_1(self):
        array = [1,2,3,4,5]
        index = 6

        result = GetElement(array, index)
        print("testcase_fail_1 passed!")
    
    def testcase_fail_2(self):
        array = ['a', 'b', 'c', 'd', 'e']
        index = 3

        result = GetElement(array, index)
        self.assertEqual(result, 'b')
        print("testcase_fail_2 passed!")

if __name__ == '__main__':
    unittest.main()
    