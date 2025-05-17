import unittest
from src.question_1.use_local_variable import use_local_variable

class TestUseLocalVariable(unittest.TestCase):
    def test_local_variable_does_not_affect_external(self):
        num = 100
        use_local_variable(num)
        # Check that `num` is still 100 after function call
        self.assertEqual(num, 100)

if __name__ == '__main__':
    unittest.main()
import unittest
from src.question_2.get_sum_of_evens import get_sum_of_evens

class TestGetSumOfEvens(unittest.TestCase):
    def test_values(self):
        self.assertEqual(get_sum_of_evens(11), 30)
        self.assertEqual(get_sum_of_evens(10), 30)
        self.assertEqual(get_sum_of_evens(8), 20)

if __name__ == '__main__':
    unittest.main()
