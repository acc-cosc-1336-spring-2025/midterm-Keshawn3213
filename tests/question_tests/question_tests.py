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
