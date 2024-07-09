import unittest

def divide(a:int, b:int) -> int:
    if b == 0:
        raise ValueError('Cannot  divide by zero.')
    return a / b

class TestMathOperation(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertRaises(ValueError, divide, 10, 0)
    

if __name__ == "__main__":
    unittest.main()