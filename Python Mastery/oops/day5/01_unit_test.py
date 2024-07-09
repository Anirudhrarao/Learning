# Unit testing is process where we test the code to make sure it works as excepted.
# Test case: A single unit of code that we want to test.
# Test suite: A collection of test cases that we want to run.
# Test runner: A program that runs the test suite.
import unittest

def add(a:int, b:int) -> int:
    return a + b 

class TestMathOperation(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(-1,1),0)
        self.assertEqual(add(0,0),0)

if __name__ == '__main__':
    unittest.main()


