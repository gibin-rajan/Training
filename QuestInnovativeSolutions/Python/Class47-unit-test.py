import unittest
from Class47 import *

class UnitTest(unittest.TestCase):
    def testing(self):
        self.assertEqual(multiply(5,5),25)
        
    def test2(self):
        self.assertTrue('ABC'.isupper())
        self.assertFalse("Abc".isupper())
        
# class UnitTest(unittest.TestCase):
#     def testing(self):
#         self.assertEqual(multiply(5,5),15)

if __name__=='__main__':
    unittest.main()